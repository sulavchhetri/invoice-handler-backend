from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Invoice(Base):
    __tablename__ = "invoices"
    
    task_id = Column(String, primary_key=True)
    task = Column(String, nullable=False)
    hours = Column(Integer, nullable=False)
    unitprice = Column(Integer, nullable=False)
    discount = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
