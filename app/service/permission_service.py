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
        # ดึงรายการ page ทั้งหมด
        pages = db.query(Page).all()

        # ดึง permission ที่ units_id นี้มี
        permissions = db.query(Permission).filter(Permission.units_id == units_id).all()

        # แปลงเป็น dict เพื่อ lookup ง่าย ๆ
        permission_page_ids = {p.page_id: p.permission_id for p in permissions}

        return_data = []
        for page in pages:
            has_permission = page.page_id in permission_page_ids
            return_data.append({
                "permission_id": permission_page_ids.get(page.page_id),
                "units_id": units_id,
                "page_id": page.page_id,
                "page_name": page.page_name,
                "permission_status": has_permission
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
