from sqlalchemy import Column, Integer, String, Boolean, Text, TIMESTAMP, func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=False)
    role = Column(String(50), default="user")
    units_id = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    created_by = Column(Text, nullable=False, default="anonimaser")
