from pydantic import BaseModel
from typing import Optional, List
from datetime import time, datetime

class UnitBase(BaseModel):
    first_name: str
    last_name: str
    position_id: int
    dept_id: Optional[int] = None
    post_code: Optional[int] = None
    address_detail: Optional[str] = None
    identify_id: Optional[str] = None
    status: Optional[str] = None
    is_active: Optional[bool] = True
    img_path: Optional[str] = None
    identify_soldier_id: Optional[str] = None
    tel: Optional[str] = None
    blood_group: Optional[str] = None
    position_detail: Optional[str] = None
    created_by: Optional[str] = "system"

class UnitCreate(UnitBase):
    pass

class UnitUpdate(UnitBase):
    pass

class UnitOut(UnitBase):
    units_id: int
    username: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True

class UnitResponse(BaseModel):
    units_id: int
    username: Optional[str] = None
    first_name: str
    last_name: str
    is_active: Optional[bool] = True
    img_path: Optional[str] = None
    position_id: Optional[int] = None
    dept_id: Optional[int] = None
    position_name_short: Optional[str] = None
    dept_name_short: Optional[str] = None

class UnitListResponse(BaseModel):
    items: List[UnitResponse]
    total: int