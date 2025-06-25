from pydantic import BaseModel
from typing import Optional, List
from datetime import time

class PermissionRespone(BaseModel):
    permission_id: Optional[int] = None
    units_id: Optional[int] = None
    page_id: Optional[int] = None
    page_name: Optional[str] = None
    permission_status: Optional[bool] = None

