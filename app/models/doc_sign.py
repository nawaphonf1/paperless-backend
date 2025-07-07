from sqlalchemy import Column, Integer, String, BigInteger, Text, Boolean, Sequence, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DocSign(Base): 
    __tablename__ = 'doc_sign'

    doc_sign_id = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        default=Sequence('doc_sign_id_seq', start=1, increment=1)
    )
    doc_id = Column(Integer, nullable=False)
    units_id = Column(Integer, nullable=False)
    path = Column(Text, nullable=False)
    sign_desc = Column(Text, nullable=True)
    created_by = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())