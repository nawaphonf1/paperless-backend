from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.auth.models import User
from app.auth.schemas import UserCreate
from fastapi import Depends, HTTPException, status
from ..database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from app.database import get_db
from app.models.permission import Permission
from app.models.page import Page

# สร้างผู้ใช้ใหม่
def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password, is_active=user.is_active, units_id=user.units_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ตรวจสอบการล็อกอิน
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

# สร้าง context สำหรับการ hash password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Secret Key และ Algorithm 

# ตั้งค่า OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "156524589523654965256526677"  # ใช้ key จริงที่ปลอดภัย
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ฟังก์ชันสำหรับสร้าง Token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# ฟังก์ชันสำหรับตรวจสอบ Token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    
def verify_token(token: str, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            )
        user = get_user_by_username(db, username)  # ใช้ db ที่เป็น Session จริง
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )

# ฟังก์ชันที่ใช้ใน route เพื่อตรวจสอบการยืนยันตัวตน
def get_current_user(db: Session, token: str = Depends(oauth2_scheme)):
    return verify_token(token, db)

def get_permission_by_units_id(db: Session, units_id: int):
    # Query the database for the permission
    permission = db.query(
        Page.page_id,
        Page.page_name,
        Permission.permission_id,
        Permission.units_id,
    ).\
    outerjoin(Permission, Page.page_id == Permission.page_id).\
    all()

    return_data = []
    if permission:
        for p in permission:
            if p.units_id == units_id:
                return_data.append({
                    "permission_id": p.permission_id,
                    "units_id": p.units_id,
                    "page_id": p.page_id,
                    "page_name": p.page_name,
                    "permission_status": True
                })
            else:
                return_data.append({
                    "permission_id": p.permission_id,
                    "units_id": p.units_id,
                    "page_id": p.page_id,
                    "page_name": p.page_name,
                    "permission_status": False
                })
    return return_data