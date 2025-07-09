from pydantic import BaseModel
from typing import Optional, List
from datetime import time, datetime

class DocBase(BaseModel):
    doc_name: str
    doc_no: str
    categories_id: int
    doc_desc: str
    critical_level: int
    doc_type: str 
    created_by: str
    updated_by: str
    created_at: datetime
    updated_at: datetime

class PathResponse(BaseModel):
    path: str
    file_name: Optional[str] = None
class DocRespone(DocBase):
    doc_id: int
    doc_recipters: Optional[List[str]] = None
    paths: Optional[List[PathResponse]] = None

    class Config:
        orm_mode = True


class DocCreate(BaseModel):
    doc_name: str
    doc_no: str
    categories_id: int
    doc_desc: str
    critical_level: int
    doc_type: str
    doc_recipters: Optional[List[int]] = None

# # Document history pagination
class DocHistorySchemas(BaseModel):
    doc_id: int
    doc_name: str
    doc_no: str
    recipters: List[str]

class DocHistoryPagination(BaseModel):
    items: List[DocHistorySchemas]
    total: int
    page: int
    size: int

    class Config:
        orm_mode = True

class HistoryCreate(BaseModel):
    doc_id: Optional[int] = None
    action: Optional[str] = None
    action_by: Optional[str] = None
    action_detail: Optional[str] = None
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None

class DocReceived(BaseModel):
    doc_id: int
    doc_name: str
    doc_no: str
    categories_id: Optional[int] = None
    doc_desc: Optional[str] = None
    critical_level: Optional[int] = None
    doc_type: str 
    sentder: str
    is_read: Optional[bool] = False
    recip_status: Optional[str] = None

class DocReceivedPagination(BaseModel):
    items: List[DocReceived]
    total: int
    page: int
    size: int

    class Config:
        orm_mode = True