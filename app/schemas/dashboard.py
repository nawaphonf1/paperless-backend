from pydantic import BaseModel
from typing import Optional, List
from datetime import time

class DashboadBase(BaseModel):
    total_docs: Optional[int] = None
    total_sending_docs: Optional[int] = None
    total_rejected_docs: Optional[int] = None
    total_submitted_docs: Optional[int] = None