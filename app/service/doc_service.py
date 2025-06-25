from sqlalchemy.orm import Session
from sqlalchemy.sql import func,and_, or_
from sqlalchemy import desc, case, and_
from typing import List

from sqlalchemy.orm import Session
# models
from app.models.doc import Doc
from app.models.doc_path import DocPath
from app.models.doc_recipter import DocRecipter
from app.models.units import Unit
from app.models.dept import Dept
from app.models.doc_history import DocHistory
from app.auth.models import User

# schemas
from app.schemas.doc import DocBase, DocRespone, DocCreate, DocHistorySchemas,DocReceived, DocReceivedPagination, DocHistoryPagination, HistoryCreate

# service
from app.service.unit_service import get_unit_by_username

class DocService:
    # creadete_doc
    @staticmethod
    def create_doc(db: Session,doc: DocCreate,current_user):
        # Check if the document already exists
        existing_doc = db.query(Doc).filter(
            Doc.doc_name == doc.doc_name,
            Doc.doc_no == doc.doc_no
        ).first()
        
        if existing_doc:
            return existing_doc
        
        new_doc = Doc(
            doc_name=doc.doc_name,
            doc_no=doc.doc_no,
            categories_id=doc.categories_id,
            doc_desc=doc.doc_desc,
            doc_type=doc.doc_type,
            critical_level=doc.critical_level,
            created_by=current_user.username,
            updated_by=current_user.username
        )
        
        db.add(new_doc)
        db.commit()
        db.refresh(new_doc)
        
        return new_doc
    # get_doc_history
    @staticmethod
    def get_doc_history(db: Session, current_user, page: int = 1, size: int = 10) -> DocHistoryPagination:
        query = db.query(Doc).filter(Doc.created_by == current_user.username)

        total = query.count()

        docs = query.order_by(desc(Doc.created_at))\
                    .offset((page - 1) * size)\
                    .limit(size)\
                    .all()

        items = []
        for doc in docs:
            if doc.doc_type == "กองร้อย":
                unit = db.query(DocRecipter.doc_recipter_id,Dept.dept_name.label("unit_name")).\
                    join(Dept, DocRecipter.units_id == Dept.dept_id).\
                    filter(DocRecipter.doc_id == doc.doc_id).all()
            else:
                unit = db.query(DocRecipter.doc_recipter_id, func.concat(Unit.first_name, ' ', Unit.last_name).label("unit_name")).\
                    join(Unit, DocRecipter.units_id == Unit.units_id).\
                    filter(DocRecipter.doc_id == doc.doc_id).all()
                
            recipter_name = [recipter.unit_name for recipter in unit]

            items.append(DocHistorySchemas(
                doc_id=doc.doc_id,
                doc_name=doc.doc_name,
                doc_no=doc.doc_no,
                recipters=recipter_name
            ))

        return DocHistoryPagination(
            items=items,
            total=total,
            page=page,
            size=size
        )
    # DocRecipter
    def create_doc_recipter(db: Session, doc_id: int, recipter_id: int, current_user):
        recipter = DocRecipter(doc_id=doc_id, units_id=recipter_id, created_by=current_user.username)
        db.add(recipter)
        db.commit()
        db.refresh(recipter)
        return recipter
    
    # get_doc_by_id
    @staticmethod
    def get_doc_by_id(db: Session, doc_id: int, current_user) -> DocRespone:
        doc = db.query(Doc).filter(Doc.doc_id == doc_id).first()
        if not doc:
            return None

        if doc.doc_type == "กองร้อย":
            unit = db.query(DocRecipter.doc_recipter_id,Dept.dept_name.label("unit_name")).\
                join(Dept, DocRecipter.units_id == Dept.dept_id).\
                filter(DocRecipter.doc_id == doc_id).all()
        else:
            unit = db.query(DocRecipter.doc_recipter_id, func.concat(Unit.first_name, ' ', Unit.last_name).label("unit_name")).\
                join(Unit, DocRecipter.units_id == Unit.units_id).\
                filter(DocRecipter.doc_id == doc_id).all()
            
        recipter_name = [recipter.unit_name for recipter in unit]

        doc_paths = db.query(DocPath).filter(DocPath.doc_id == doc_id).all()
        paths = [d.path for d in doc_paths]

        return DocRespone(
            doc_id=doc.doc_id,
            doc_name=doc.doc_name,
            doc_no=doc.doc_no,
            categories_id=doc.categories_id,
            doc_desc=doc.doc_desc,
            doc_type=doc.doc_type,
            critical_level=doc.critical_level,
            created_by=doc.created_by,
            updated_by=doc.updated_by,
            created_at=doc.created_at,
            updated_at=doc.updated_at,
            doc_recipters=recipter_name,
            paths=paths
        )

    # get_doc_history_by_doc_id
    @staticmethod
    def get_doc_history_by_doc_id(db: Session, doc_id: int) -> List[HistoryCreate]:
        doc_history = db.query(
            Doc.doc_id,
            DocHistory.action,
            DocHistory.action_by,
            DocHistory.action_detail,
            DocHistory.created_at,
            DocHistory.created_by
            ).\
            join(DocHistory, Doc.doc_id == DocHistory.doc_id).\
            filter(Doc.doc_id == doc_id).all()
        if not doc_history:
            return []
        return [
            HistoryCreate(
                doc_id=history.doc_id,
                action=history.action,
                action_by=history.action_by,
                action_detail=history.action_detail,
                created_at=history.created_at,
                created_by=history.created_by
            ) for history in doc_history
        ]

    # get_received_docs
    @staticmethod
    def get_received_docs(db: Session, current_user, page: int = 1, size: int = 10) ->DocReceivedPagination:

        unit = get_unit_by_username(db, current_user.username)


        query = db.query(
                Doc.doc_id,
                Doc.doc_name,
                Doc.doc_no,
                Doc.doc_type,
                Doc.created_by,
                DocRecipter.units_id,
                DocRecipter.doc_recipter_id,
                DocRecipter.is_read,
                DocRecipter.recip_status,         
            ).join(DocRecipter, Doc.doc_id == DocRecipter.doc_id).filter(
            or_(
                and_(Doc.doc_type == "กองร้อย", DocRecipter.units_id == unit.dept_id),
                and_(Doc.doc_type != "กองร้อย", DocRecipter.units_id == unit.units_id)
            )
        )
        total = query.count()
        docs = query.order_by(desc(Doc.created_at))\
                    .offset((page - 1) * size)\
                    .limit(size)\
                    .all()
        items = []
        for doc in docs:
            user = db.query(Unit).\
                join(User, Unit.units_id == User.units_id).\
                filter(User.username == doc.created_by).first()
            
            items.append(DocReceived(
                doc_id=doc.doc_id,
                doc_name=doc.doc_name,
                doc_no=doc.doc_no,
                doc_type=doc.doc_type,
                is_read=doc.is_read,
                recip_status=doc.recip_status,
                sentder=user.first_name + ' ' + user.last_name if user else "Unknown",
            ))

        return DocReceivedPagination(
            items=items,
            total=total,
            page=page,
            size=size
        )



    # submit
    @staticmethod
    def submit_doc(db: Session, doc_id: int, current_user) -> DocRespone:
        doc = db.query(Doc).filter(Doc.doc_id == doc_id).first()
        if not doc:
            return None
        
        submit_text = f"เอกสาร '{doc.doc_name}' ถูกรับโดย {current_user.username}"
        
        units_id = None
        unit = db.query(Unit).filter(Unit.units_id == current_user.units_id).first()

        if doc.doc_type == "กองร้อย":
            units_id = unit.dept_id if unit else None
        else:
            units_id = unit.units_id if unit else None

        # update doc_recipter
        doc_recipter = DocService.update_doc_recipter(db, doc_id, units_id, current_user, "รับเอกสาร")

        # update doc history
        doc_history = DocService.update_doc_history(db, doc_id, "รับเอกสาร" , current_user, submit_text)
    
    def reject_doc(db: Session, doc_id: int, current_user, reject_text) -> DocRespone:
        doc = db.query(Doc).filter(Doc.doc_id == doc_id).first()
        if not doc:
            return None
                
        units_id = None
        unit = db.query(Unit).filter(Unit.units_id == current_user.units_id).first()

        if doc.doc_type == "กองร้อย":
            units_id = unit.dept_id if unit else None
        else:
            units_id = unit.units_id if unit else None

        # update doc_recipter
        doc_recipter = DocService.update_doc_recipter(db, doc_id, units_id, current_user, "ปฏิเสธเอกสาร", reject_text)

        # update doc history
        doc_history = DocService.update_doc_history(db, doc_id, "ปฏิเศษ" , current_user, reject_text)

    def update_doc_recipter(db: Session, doc_id: int, units_id: int, current_user, action: str, doc_recipter_text:str = None) -> DocRecipter:
        doc_recipter = db.query(DocRecipter).filter(
            DocRecipter.doc_id == doc_id,
            DocRecipter.units_id == units_id
        ).first()
        if doc_recipter:
            doc_recipter.is_read = True
            doc_recipter.recip_status = action
            doc_recipter.recipter_desc = doc_recipter_text if doc_recipter_text else None
            doc_recipter.updated_by = current_user.username
            db.commit()
            db.refresh(doc_recipter)
    
    def update_doc_history(db: Session, doc_id: int, action: str, current_user, reject_text: str = None) -> DocHistory:
        if reject_text:
            reject_text = reject_text
        else:
            reject_text = f"เอกสาร '{doc_id}' ถูก {action}"
        doc_history = DocHistory(
            doc_id=doc_id,
            action=action,
            action_by=current_user.username,
            action_detail=reject_text,
            created_by=current_user.username
        )
        db.add(doc_history)
        db.commit()
        db.refresh(doc_history)
        return doc_history
