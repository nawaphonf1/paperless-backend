from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from datetime import timedelta
from app.database import get_db
from app.auth.services import create_user, authenticate_user, create_access_token, get_permission_by_units_id
from app.auth.schemas import UserCreate, Token, LoginRequest
from app.auth.dependencies import get_current_user
from app.models.units import Unit
from app.models.dept import Dept
from app.models.position import Position


from sqlalchemy.sql import func,and_, or_

router = APIRouter()

@router.post("/register", response_model=Token)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_in_db = create_user(db, user)
    access_token = create_access_token(data={"sub": user_in_db.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/auth/", response_model=Token)
def login_user(
    username: str = Form(...),  # รับข้อมูลจาก Form Data
    password: str = Form(...),  # รับข้อมูลจาก Form Data
    db: Session = Depends(get_db)
):
    # ตรวจสอบข้อมูลผู้ใช้
    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    # สร้าง token และส่งกลับ
    access_token = create_access_token(data={"sub": user.username})

    permission = get_permission_by_units_id(db=db, units_id=user.units_id)
    
    unit_name = None
    unit_img = None

    unit = db.query(
            Unit.img_path,
            func.concat(Position.position_name_short, ' ', Unit.first_name, ' ', Unit.last_name).label("unit_name")
            ).\
                select_from(Unit).\
                join(Position, Position.position_id == Unit.position_id).\
                filter(Unit.units_id == user.units_id).\
                first()

    if unit:
        unit_name = unit.unit_name
        unit_img = unit.img_path

    return {
        "access_token": access_token, 
        "token_type": "bearer", 
        "role": user.role,
        "permission": permission,
        "unit_name": unit_name,
        "unit_img": unit_img
        }