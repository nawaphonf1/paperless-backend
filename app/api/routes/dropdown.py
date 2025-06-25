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

# import service
from app.service.dropdown_service import DropdownService

# import schemas
from app.schemas.dropdown import DropdownRespone

router = APIRouter()


# dropdown position
@router.get("/position", response_model=List[DropdownRespone])
def get_position(
    word: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    items = DropdownService.get_position(db=db, word=word)
    return items

# dropdown department
@router.get("/department", response_model=List[DropdownRespone])
def get_department(
    word: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    items = DropdownService.get_department(db=db, word=word)
    return items

# dropdown cetegory
@router.get("/category", response_model=List[DropdownRespone])
def get_category(
    word: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    items = DropdownService.get_category(db=db, word=word)
    return items

# dropdown unit
@router.get("/unit", response_model=List[DropdownRespone])
def get_unit(
    word: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    items = DropdownService.get_unit(db=db, word=word)
    return items