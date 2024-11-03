from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Invoice(Base):
    __tablename__ = "invoices"

    task_id = Column(String, primary_key=True)
    task = Column(String, nullable=False)
    hours = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    discount = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)


class Tasks(Base):
    __tablename__ = "tasks"
    task_id = Column(String, primary_key=True)
    parents = Column(ARRAY(String), nullable=True, default=list)
