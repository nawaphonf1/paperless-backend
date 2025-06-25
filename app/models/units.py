from sqlalchemy import Column, Integer, String, BigInteger, Boolean, Text, DateTime, func
from app.database import Base

class Unit(Base):
    __tablename__ = "units"

    units_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    position_id = Column(Integer, nullable=False)
    dept_id = Column(Integer)
    post_code = Column(BigInteger)
    address_detail = Column(Text)
    identify_id = Column(Text)
    status = Column(Text)
    is_active = Column(Boolean, nullable=False, default=True)
    img_path = Column(Text)
    identify_soldier_id = Column(Text)
    tel = Column(Text)
    blood_group = Column(Text)
    position_detail = Column(Text)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    created_by = Column(Text, nullable=False)
