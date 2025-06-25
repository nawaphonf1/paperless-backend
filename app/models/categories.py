from sqlalchemy import Column, Integer, String, BigInteger, Text, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Categories(Base):
    __tablename__ = 'categories'

    categories_id = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        default=Sequence('categories_id_seq', start=1, increment=1)
    )
    categories_name = Column(String(100), nullable=False)
    categories_desc = Column(String(100), nullable=False)