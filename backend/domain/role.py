from .util import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID


class Role(BaseModel):
    __tablename__ = 'role'
    id = Column(UUID, primary_key=True)
    name = Column(String)
