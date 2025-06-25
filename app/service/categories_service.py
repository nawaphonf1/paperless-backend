from sqlalchemy.orm import Session
from sqlalchemy.sql import func,and_, or_
from sqlalchemy import desc

from sqlalchemy.orm import Session
# models
from app.models.position import Position
from app.models.dept import Dept
from app.auth.models import User
from app.models.units import Unit
from app.models.categories import Categories

# schemas
from app.schemas.units import UnitCreate, UnitOut
from app.schemas.categories import CategoriesRespone

class CategoriesService:
    @staticmethod
    def get_categories(db: Session, word: str = None):
        cretegories_query = db.query(
            Categories.categories_id,
            Categories.categories_name,
            Categories.categories_desc
        )
        if word:
            cretegories_query = cretegories_query.filter(Categories.categories_name.ilike(f"%{word}%"))
        
        return cretegories_query.order_by(Categories.categories_name).all()
    
    # create_category
    @staticmethod
    def create_category(
        db: Session,
        categories_name: str,
        categories_desc: str = None
    ):
        # Check if the category already exists
        existing_category = db.query(Categories).filter(
            Categories.categories_name == categories_name
        ).first()
        
        if existing_category:
            return existing_category
        
        new_category = Categories(
            categories_name=categories_name,
            categories_desc=categories_desc
        )
        
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        
        return new_category