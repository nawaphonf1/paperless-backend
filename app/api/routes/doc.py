from fastapi import APIRouter, Depends, HTTPException,  File, UploadFile, Query
from pathlib import Path
import shutil
from typing import List
from fastapi.responses import StreamingResponse
from datetime import date

from sqlalchemy.orm import Session
from ...database import SessionLocal
from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.database import get_db
from typing import Optional
from urllib.parse import quote

# import service
from app.service.doc_service import DocService
from app.service.unit_service import get_unit_by_username

# import schemas
from app.schemas.doc import DocBase, DocRespone, DocCreate, DocHistoryPagination, HistoryCreate

# import models
from app.models.doc import Doc
from app.models.doc_path import DocPath
from app.models.doc_recipter import DocRecipter
from app.models.doc_history import DocHistory
# DocSign
from app.models.doc_sign import DocSign

from base64 import b64decode

router = APIRouter()
# receive doc
@router.get("/receive")
def receive_doc(
    page: int = Query(1, ge=1, description="Page number for pagination"),
    size: int = Query(10, ge=1, le=100, description="Number of items per page"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get documents received by the current user with pagination.
    """
    
    docs = DocService.get_received_docs(db, current_user, page, size)
    if not docs:
        raise HTTPException(status_code=404, detail="No received documents found")
    return docs

# crated doc
@router.post("/", response_model=DocRespone)
def create_doc(
    doc: DocCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Create a new document.
    """
    crated_doc = DocService.create_doc(db, doc, current_user)

    # created doc history
    if crated_doc:
        doc_history = DocHistory(
            doc_id=crated_doc.doc_id,
            action="สร้างเอกสาร",
            action_by=current_user.username,
            action_detail=f"สร้างเอกสาร '{crated_doc.doc_name}' ",
            created_by=current_user.username
        )
        db.add(doc_history)
        db.commit()
        db.refresh(doc_history)


    # crate doc recipters
    if doc.doc_recipters:
        # Check if the recipter already exists
        existing_recipter = db.query(DocRecipter).filter(
            DocRecipter.doc_id == crated_doc.doc_id
        ).delete()
        for recipter_id in doc.doc_recipters:
            DocService.create_doc_recipter(db, crated_doc.doc_id, recipter_id, current_user)

    return crated_doc

# sent doc history
@router.get("/history", response_model=DocHistoryPagination)
def get_doc_history(
    page: int = Query(1, ge=1, description="Page number for pagination"),
    size: int = Query(10, ge=1, le=100, description="Number of items per page"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get document history with optional date filtering.
    """
    docs = DocService.get_doc_history(db, current_user, page, size)
    return docs

# upload doc file
@router.post("/upload/{doc_id}")
def upload_doc_files(
    doc_id: int,
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Upload multiple document files.
    """
    # ตรวจสอบว่าเอกสารนี้มีอยู่หรือไม่
    existing_doc = db.query(Doc).filter(Doc.doc_id == doc_id).first()
    if not existing_doc:
        raise HTTPException(status_code=404, detail="Document not found")

    upload_dir = Path("uploads") / str(existing_doc.doc_name)
    upload_dir.mkdir(parents=True, exist_ok=True)

    saved_paths = []

    for file in files:
        file_path = upload_dir / file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # สร้าง record ใน DocPath
        doc_path = DocPath(doc_id=doc_id, path=str(file_path), created_by=current_user.username)
        db.add(doc_path)
        saved_paths.append(str(file_path))

    db.commit()

    return {
        "message": f"{len(saved_paths)} files uploaded successfully.",
        "files": saved_paths
    }

# get doc by id
@router.get("/{doc_id}", response_model=DocRespone)
def get_doc_by_id(
    doc_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    doc = DocService.get_doc_by_id(db, doc_id, current_user)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc

@router.get("/download/{path:path}")  # <- ต้องระบุ :path เพื่อรองรับ path ที่มี /
def download_doc_file(
    path: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    file_path = Path(path)

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found on server")

    filename = file_path.name
    quoted_filename = quote(filename)  # เปลี่ยนชื่อไฟล์เป็น URL-encoded

    return StreamingResponse(
        file_path.open("rb"),
        media_type="application/octet-stream",
        headers={
            # ป้องกันปัญหาชื่อไฟล์ภาษาไทย
            "Content-Disposition": f"attachment; filename*=UTF-8''{quoted_filename}"
        }
    )

    # get doc history by doc_id
@router.get("/history/{doc_id}", response_model=List[HistoryCreate])
def get_doc_history_by_doc_id(
    doc_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get document history by document ID with pagination.
    """
    docs = DocService.get_doc_history_by_doc_id(db, doc_id)
    if not docs:
        raise HTTPException(status_code=404, detail="Document history not found")
    return docs

# submit doc
@router.post("/action/{doc_id}")
def action_doc(
    doc_id: int,
    action: str,
    reject_text: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Perform an action on a document (e.g., submit, approve, reject).
    """
    doc = db.query(Doc).filter(Doc.doc_id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    if action == "submit":
        submit_doc = DocService.submit_doc(db, doc_id, current_user)
    
    if action == "reject":
        reject_doc = DocService.reject_doc(db, doc_id, current_user,reject_text)

# upload doc file
@router.post("/upload/sign/{doc_id}")
def upload_doc_files(
    doc_id: int,
    description: Optional[str] = None,
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Upload multiple document files.
    """
    # ตรวจสอบว่าเอกสารนี้มีอยู่หรือไม่
    existing_doc = db.query(Doc).filter(Doc.doc_id == doc_id).first()
    if not existing_doc:
        raise HTTPException(status_code=404, detail="Document not found")
    
    units = get_unit_by_username(db, current_user.username)

    upload_dir = Path("sign") / str(existing_doc.doc_name)
    upload_dir.mkdir(parents=True, exist_ok=True)

    saved_paths = []

    for file in files:
        file_path = upload_dir / file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # สร้าง record ใน DocPath
        doc_path = DocSign(
            doc_id=doc_id,
            units_id = units.units_id, 
            path=str(file_path), 
            sign_desc=description,
            created_by=current_user.username)
        db.add(doc_path)
        saved_paths.append(str(file_path))

    db.commit()

    return {
        "message": f"{len(saved_paths)} files uploaded successfully.",
        "files": saved_paths
    }

# get doc sign by doc_id
@router.get("/sign/{doc_id}")
def get_doc_sign_by_doc_id(
    doc_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get document sign by document ID.
    """
    doc_signs = db.query(DocSign).filter(DocSign.doc_id == doc_id).all()
    if not doc_signs:
        raise HTTPException(status_code=404, detail="Document sign not found")
    return doc_signs

# del doc_sign by doc_sign_id
@router.delete("/sign/{doc_sign_id}")
def delete_doc_sign(
    doc_sign_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Delete a document sign by its ID.
    """
    doc_sign = db.query(DocSign).filter(DocSign.doc_sign_id == doc_sign_id).first()
    if not doc_sign:
        raise HTTPException(status_code=404, detail="Document sign not found")

    db.delete(doc_sign)
    db.commit()

    # Delete the file from the filesystem
    file_path = Path(doc_sign.path)
    if file_path.exists():
        file_path.unlink()
    else:
        raise HTTPException(status_code=404, detail="File not found on server")

    return {"message": "Document sign deleted successfully"}
