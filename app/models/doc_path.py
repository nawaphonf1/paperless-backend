from sqlalchemy import Column, Integer, String, BigInteger, Text, Boolean, Sequence, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DocPath(Base):
    __tablename__ = 'doc_path'

    doc_path_id = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        default=Sequence('doc_path_id_seq', start=1, increment=1)
    )
    doc_id = Column(Integer, nullable=False)
    path = Column(String(100), nullable=False)
    created_by = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())