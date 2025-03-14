from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Table, Column, Integer, String, DateTime, func
from db.conn import engine, Base


class Product(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(30), nullable=False)
    description = Column(String(100), unique=True, nullable=False, index=True)
    location = Column(String(100), unique=True, nullable=False, index=True)
    price = Column(Integer(30), nullable=False)
    created_at = Column(DateTime, default= func.now() )
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


