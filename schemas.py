from typing import List, Optional

from pydantic import BaseModel
from datetime import datetime, date


class User(BaseModel):

    email: str
    password: str
    is_active: bool

    class Config:
        orm_mode = True


class Case(BaseModel):
    Branch: str
    Method: str
    Date: date
    Time: str
    Category: str
    SubCategory: str
    Priority: str
    Nature: str
    Manager: str
    Reporter: str
    Status: str

    class Config:
        orm_mode = True


class GetCase(BaseModel):
    id: int
    Branch: str
    Method: str
    Date: date
    Time: str
    Category: str
    SubCategory: str
    Priority: str
    Nature: str
    Manager: str
    Reporter: str
    Status: str

    class Config:
        orm_mode = True
