from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import get_class_by_table

Base = declarative_base()

""" IGNORE - internal testing """


class User(Base):
    __tablename__ = 'entity'
    id = Column(Integer, primary_key=True)
    name = Column(String)


cls = get_class_by_table(Base, User.__table__)  # User class given table entity
print(cls)
