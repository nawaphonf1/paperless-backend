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
from app.service.dashboad_service import DashboadService

router = APIRouter()
# get dashboard data
@router.get("/total")
def get_dashboard_data(
    date_start: Optional[date] = None,
    date_end: Optional[date] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get dashboard data for the current user.
    """
    try:
        dashboard_data = DashboadService.get_dashboard_data(db, current_user, date_start, date_end)
        return dashboard_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# to do list
@router.get("/to-do-list")
def get_to_do_list(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get to-do list for the current user.
    """
    try:
        to_do_list = DashboadService.get_to_do_list(db, current_user)
        return to_do_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




