from sqlalchemy import Column, Integer, String, BigInteger, Text, Boolean, Sequence, Time, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Permission(Base):
    __tablename__ = 'permission'

    permission_id = Column(
        Integer, 
        primary_key=True,
        index=True, 
        default=Sequence('permission_id_seq', start=1, increment=1)
    )
    units_id = Column(Integer, nullable=False)
    page_id = Column(Integer, nullable=False)
    created_at = Column(Time, nullable=False, server_default=func.now())
    created_by = Column(Text, nullable=False)