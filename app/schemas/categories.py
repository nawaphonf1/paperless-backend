from pydantic import BaseModel
from typing import Optional, List
from datetime import time

class CategoriesBase(BaseModel):
    categories_name: Optional[str] = None
    categories_desc: Optional[str] = None

class CategoriesRespone(CategoriesBase):
    categories_id: int

