from fastapi import APIRouter, Depends, HTTPException,  File, UploadFile, Query
from pathlib import Path
import shutil
from typing import List
from fastapi.responses import StreamingResponse
from datetime import date

from sqlalchemy.orm import Session
from ...database import SessionLocal
from app.models.units import Unit
from app.schemas.units import UnitCreate, UnitOut, UnitResponse, UnitListResponse, UnitUpdate
from app.auth.schemas import UserCreate

from app.auth.dependencies import get_current_user
from app.auth.models import User
from app.database import get_db
from typing import Optional

# import service
from app.service import unit_service
from app.auth.services import create_user
router = APIRouter()


@router.post("/", response_model=UnitOut)
def create_unit(unit: UnitCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    units = unit_service.create_unit(db=db, unit=unit)
    # crate_user
    user = create_user(db=db, user=UserCreate(
        username=unit.identify_soldier_id,
        password=unit.identify_soldier_id,
        units_id=units.units_id,
        is_active=True
    ))
    return units

# get all units by offset and limit
@router.get("/", response_model=UnitListResponse)
def get_units(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    items = unit_service.get_units(db=db, skip=skip, limit=limit)
    total = unit_service.get_units_count(db=db)
    return {"items": items, "total": total}


# get unit by id
@router.get("/{unit_id}", response_model=UnitResponse)
def get_unit_by_id(unit_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    db_unit = unit_service.get_unit_by_id(db=db, unit_id=unit_id)
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return db_unit

# update unit by id
@router.put("/{unit_id}", response_model=UnitOut)
def update_unit(
    unit_id: int,
    unit: UnitUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    db_unit = db.query(Unit).filter(Unit.units_id == unit_id).first()

    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit_service.update_unit(db=db, db_unit=db_unit, unit=unit, current_user=current_user)

# delete unit by id
@router.delete("/{unit_id}", response_model=UnitOut)
def delete_unit(
    unit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # current_user จะได้รับค่าผู้ใช้จากการตรวจสอบ token
    db_unit = db.query(Unit).filter(Unit.units_id == unit_id).first()

    # del user by units_id
    db_user = db.query(User).filter(User.units_id == unit_id).first()

    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    
    db.delete(db_unit)
    db.delete(db_user)

    db.commit()
    return db_unit