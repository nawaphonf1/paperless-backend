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
from app.service.permission_service import PermissionService

# import schemas
from app.schemas.permission import PermissionRespone

router = APIRouter()

# get permission
@router.get("/{units_id}", response_model=List[PermissionRespone])
def get_permission(
    units_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    permission = PermissionService.get_permission_by_units_id(db=db, units_id=units_id)
    if permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission

# update permission
@router.put("/{units_id}", response_model=List[PermissionRespone])
def update_permission(
    units_id: int,
    permission: List[PermissionRespone],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    permission = PermissionService.update_permission(current_user=current_user, db=db, units_id=units_id, permission=permission)
    if permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission