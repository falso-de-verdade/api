"""Basic One-To-Many relationship configuration in SQLAlchemy.

This is taken from the official SQLAlchemy documentation:
https://docs.sqlalchemy.org/en/rel_1_1/orm/basic_relationships.html#one-to-many
"""

from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    _created = Column(DateTime, default=func.now())
    _updated = Column(DateTime, default=func.now(), onupdate=func.now())
    _etag = Column(String(60))
