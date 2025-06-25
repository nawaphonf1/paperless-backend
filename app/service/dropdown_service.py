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

class DropdownService:
    # dropdown position
    @staticmethod
    def get_position(db: Session, word: str = None):
        if word:
            return db.query(
                Position.position_id.label("value"),
                Position.position_name_short.label("label"),
                Position.position_name,
            ).filter(
                or_(
                    Position.position_name_short.ilike(f"%{word}%"),
                    Position.position_name.ilike(f"%{word}%")
                )
            ).order_by(Position.position_seq).all()
        else:
            return db.query(
                Position.position_id.label("value"),
                Position.position_name_short.label("label"),
                Position.position_name,
            ).order_by(Position.position_seq).all()
        
    # dropdown department
    @staticmethod
    def get_department(db: Session, word: str = None):
        if word:
            return db.query(
                Dept.dept_id.label("value"),
                Dept.dept_name_short.label("label"),
                Dept.dept_name,
            ).filter(
                or_(
                    Dept.dept_name_short.ilike(f"%{word}%"),
                    Dept.dept_name.ilike(f"%{word}%")
                )
            ).all()
        else:
            return db.query(
                Dept.dept_id.label("value"),
                Dept.dept_name_short.label("label"),
                Dept.dept_name,
            ).all()

    # dropdown Categories
    @staticmethod
    def get_category(db: Session, word: str = None):
        if word:
            return db.query(
                Categories.categories_id.label("value"),
                Categories.categories_name.label("label"),
                Categories.categories_desc,
            ).filter(
                or_(
                    Categories.categories_name.ilike(f"%{word}%"),
                    Categories.categories_desc.ilike(f"%{word}%")
                )
            ).all()
        else:
            return db.query(
                Categories.categories_id.label("value"),
                Categories.categories_name.label("label"),
                Categories.categories_desc,
            ).all()

    # dropdown unit
    @staticmethod
    def get_unit(db: Session, word: str = None):
        if word:
            return db.query(
                Unit.units_id.label("value"),
                func.concat(Position.position_name_short, Unit.first_name, ' ', Unit.last_name).label("label"),
            ).filter(
                or_(
                    Unit.first_name.ilike(f"%{word}%"),
                    Unit.last_name.ilike(f"%{word}%")
                )
            ).\
            join(Position, Position.position_id == Unit.position_id).all()
        else:
            return db.query(
                Unit.units_id.label("value"),
                func.concat(Position.position_name_short, Unit.first_name, ' ', Unit.last_name).label("label"),
            ).\
            join(Position, Position.position_id == Unit.position_id).all()
    
