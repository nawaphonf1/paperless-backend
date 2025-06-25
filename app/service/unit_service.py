from sqlalchemy.orm import Session
from sqlalchemy.sql import func,and_, or_
from sqlalchemy import desc

from sqlalchemy.orm import Session
# models
from app.models.position import Position
from app.models.dept import Dept
from app.auth.models import User
from app.models.units import Unit
# schemas

from app.schemas.units import UnitCreate, UnitOut, UnitUpdate



def create_unit(db: Session, unit: UnitCreate):
    db_unit = Unit(**unit.dict())
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit

# get all units by offset and limit
def get_units(db: Session, skip: int = 0, limit: int = 100):
    return db.query(
        Unit.units_id,
        Unit.first_name,
        Unit.last_name,
        Unit.position_id,
        Unit.dept_id,
        Position.position_name_short,
        Dept.dept_name_short,
        User.username
        ).\
        outerjoin(Position, Unit.position_id == Position.position_id).\
        outerjoin(Dept, Unit.dept_id == Dept.dept_id).\
        outerjoin(User, Unit.units_id == User.units_id).\
        offset(skip).limit(limit).all()     

def get_units_count(db: Session):
    return db.query(Unit).count()


# get_unit_by_id
def get_unit_by_id(db: Session, unit_id: int):
    return db.query(
        Unit.units_id,
        Unit.first_name,
        Unit.last_name,
        Unit.position_id,
        Unit.dept_id,
        Position.position_name_short,
        Dept.dept_name_short,
        User.username
    ).\
    outerjoin(Position, Unit.position_id == Position.position_id).\
    outerjoin(Dept, Unit.dept_id == Dept.dept_id).\
    outerjoin(User, Unit.units_id == User.units_id).\
    filter(Unit.units_id == unit_id).first()

# update unit by id
def update_unit(db: Session, db_unit: Unit, unit: UnitUpdate, current_user: User):
    # สร้าง dict จาก input โดยไม่รวม created_by
    update_data = unit.dict(exclude={"created_by"})

    # อัปเดตฟิลด์จาก input
    for key, value in update_data.items():
        setattr(db_unit, key, value)

    # เซ็ต created_by จาก token โดยตรง
    db_unit.created_by = current_user.username

    db.commit()
    db.refresh(db_unit)
    return db_unit

def get_unit_by_username(db: Session, username: str):
    units = db.query(User.units_id).filter(User.username == username).first()

    return db.query(Unit).filter(Unit.units_id == units.units_id).first()