from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import relationship
from datetime import date, datetime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)


class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    Branch = Column(String)
    Method = Column(String)
    Date = Column(Date, default=date.today())
    Time = Column(String)
    Category = Column(String)
    SubCategory = Column(String)
    Priority = Column(String)
    Nature = Column(String)
    Manager = Column(String)
    Reporter = Column(String)
    Status = Column(String)
