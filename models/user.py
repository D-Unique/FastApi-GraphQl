from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Table, Column, Integer, String
from db.conn import engine, Base


class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(100), unique=True)
    password = Column(String(30))


