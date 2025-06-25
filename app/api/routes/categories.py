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
from app.service.categories_service import CategoriesService

# import schemas
from app.schemas.categories import CategoriesRespone, CategoriesBase

router = APIRouter()


# get categories
@router.get("/", response_model=List[CategoriesRespone])
def get_categories(
    word: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    items = CategoriesService.get_categories(db=db, word=word)
    return items

# create category
@router.post("/", response_model=CategoriesRespone)
def create_category(
    categories :CategoriesBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    if not categories.categories_name:
        raise HTTPException(status_code=400, detail="Category name is required")
    
    item = CategoriesService.create_category(
        db=db,
        categories_name=categories.categories_name,
        categories_desc=categories.categories_desc
    )
    return item