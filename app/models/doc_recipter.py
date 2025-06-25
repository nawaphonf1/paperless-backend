from sqlalchemy import Column, Integer, String, BigInteger, Text, Boolean, Sequence, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DocRecipter(Base):
    __tablename__ = 'doc_recipter'

    doc_recipter_id = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        default=Sequence('doc_recipter_id_seq', start=1, increment=1)
    )
    doc_id = Column(Integer, nullable=False)
    units_id = Column(Integer, nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    recip_status = Column(String(20), nullable=False, default='รอดำเนินการ')
    recipter_desc = Column(Text, nullable=True)
    created_by = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())