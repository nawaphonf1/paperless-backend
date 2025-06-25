from sqlalchemy.orm import Session
from sqlalchemy.sql import func,and_, or_
from sqlalchemy import desc

from sqlalchemy.orm import Session
# models
from app.models.permission import Permission
from app.models.page import Page
from app.models.units import Unit
from app.auth.models import User
# schemas

from app.schemas.units import UnitCreate, UnitOut

class PermissionService:
    def get_permission_by_units_id(db: Session, units_id: int):
        # Query the database for the permission
        permission = db.query(
            Page.page_id,
            Page.page_name,
            Permission.permission_id,
            Permission.units_id,
        ).\
        outerjoin(Permission, Page.page_id == Permission.page_id).\
        all()

        return_data = []
        if permission:
            for p in permission:
                if p.units_id == units_id:
                    return_data.append({
                        "permission_id": p.permission_id,
                        "units_id": p.units_id,
                        "page_id": p.page_id,
                        "page_name": p.page_name,
                        "permission_status": True
                    })
                else:
                    return_data.append({
                        "permission_id": p.permission_id,
                        "units_id": p.units_id,
                        "page_id": p.page_id,
                        "page_name": p.page_name,
                        "permission_status": False
                    })
        return return_data
    
    # update_permission
    def update_permission(current_user: User, db: Session, units_id: int, permission: list):
        # ลบสิทธิเก่าทิ้ง
        db.query(Permission).filter(Permission.units_id == units_id).delete()

        # เพิ่มสิทธิใหม่เฉพาะที่มี permission_status == True
        for p in permission:
            new_permission = Permission(
                units_id=units_id,
                page_id = p.page_id
,
                created_by=current_user.username
            )
            db.add(new_permission)

        db.commit()

        # คืนค่ารายการใหม่ (optional)
        return db.query(
            Permission.permission_id,
            Permission.units_id,
            Permission.page_id,
            Page.page_name
        ).outerjoin(Page, Permission.page_id == Page.page_id).filter(
            Permission.units_id == units_id
        ).all()
