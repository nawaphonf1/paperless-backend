from sqlalchemy import Column, Integer, String, BigInteger, Text, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Page(Base):
    __tablename__ = 'page'

    page_id = Column(
        Integer, 
        primary_key=True,
        index=True, 
        default=Sequence('page_id_seq', start=1, increment=1)
    )
    page_no = Column(Integer, nullable=False)
    page_name = Column(String(100), nullable=False)