from sqlalchemy import Column, Integer, String, BigInteger, Text, Boolean, Sequence,Time, func, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DocHistory(Base):
    __tablename__ = 'doc_history'

    doc_history_id = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        default=Sequence('doc_history_id_seq', start=1, increment=1)
    )
    doc_id = Column(Integer, nullable=False)
    action = Column(String(50), nullable=False)
    action_by = Column(String(50), nullable=False)
    action_detail = Column(Text, nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    created_by = Column(String(50), nullable=False)