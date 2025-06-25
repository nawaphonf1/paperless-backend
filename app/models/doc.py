from sqlalchemy import Column, Integer, String, Text, Sequence, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Doc(Base):
    __tablename__ = 'doc'

    doc_id = Column(
        Integer,
        primary_key=True,
        index=True,
        default=Sequence('doc_id_seq', start=1, increment=1)
    )
    doc_name = Column(String(100), nullable=False)
    doc_no = Column(String(100), nullable=False)
    categories_id = Column(Integer, nullable=False)
    doc_desc = Column(String(100), nullable=False)
    critical_level = Column(Integer, nullable=False)
    doc_type = Column(String(20), nullable=False)
    created_by = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_by = Column(Text, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=func.now())
