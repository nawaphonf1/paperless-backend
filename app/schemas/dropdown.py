from pydantic import BaseModel
from typing import Optional, List
from datetime import time

class DropdownRespone(BaseModel):
    value: int
    label: str