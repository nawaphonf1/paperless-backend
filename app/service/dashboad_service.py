from sqlalchemy.orm import Session
from sqlalchemy.sql import func,and_, or_
from sqlalchemy import desc

from sqlalchemy.orm import Session
# models
from app.models.doc import Doc
from app.models.doc_history import DocHistory
from app.models.doc_recipter import DocRecipter
from app.auth.models import User
from app.models.units import Unit


# schemas
from app.schemas.dashboard import DashboadBase

class DashboadService:
    # get_dashboard_data  -> DashboadBase
    @staticmethod
    def get_dashboard_data(db: Session, current_user: User, date_start=None, date_end=None): 
        unit = db.query(Unit).filter(Unit.units_id == current_user.units_id).first()
        # get doc 
        doc = db.query(Doc).\
            join(DocRecipter, Doc.doc_id == DocRecipter.doc_id).\
            filter(
            or_(
                and_(Doc.doc_type == "กองร้อย", DocRecipter.units_id == unit.dept_id),
                and_(Doc.doc_type != "กองร้อย", DocRecipter.units_id == unit.units_id)
            )
        )

        if date_start and date_end:
            doc = doc.filter(Doc.created_at.between(date_start, date_end))
        
        total_docs_data= doc
        total_sending_docs_data = doc
        total_rejected_docs_data = doc
        total_submitted_docs_data = doc
        total_pending_docs_data = doc


        return {
            "total_docs": total_docs_data.count(),
            "total_sending_docs_data": total_sending_docs_data.filter(Doc.created_by == current_user.username).count(),
            "total_rejected_docs_data": total_rejected_docs_data.filter(DocRecipter.recip_status == "ปฏิเสธเอกสาร").count(),
            "total_submitted_docs_data": total_submitted_docs_data.filter(DocRecipter.recip_status == "รับเอกสาร").count(),
            "total_pending_docs_data": total_pending_docs_data.filter(DocRecipter.recip_status == "รอดำเนินการ").count()
        }
    

    # get_to_do_list
    @staticmethod
    def get_to_do_list(db: Session, current_user: User):
        unit = db.query(Unit).filter(Unit.units_id == current_user.units_id).first()
        # get doc 
        doc = db.query(Doc).\
            join(DocRecipter, Doc.doc_id == DocRecipter.doc_id).\
            filter(
            or_(
                and_(Doc.doc_type == "กองร้อย", DocRecipter.units_id == unit.dept_id),
                and_(Doc.doc_type != "กองร้อย", DocRecipter.units_id == unit.units_id)
            )
        ).\
        filter(DocRecipter.recip_status == "รอดำเนินการ").\
        order_by(desc(Doc.created_at)).all()

        return doc