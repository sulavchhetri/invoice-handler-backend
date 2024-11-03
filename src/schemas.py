from pydantic import BaseModel
from typing import Dict


class InvoiceItem(BaseModel):
    task: str
    hours: int
    unit_price: int
    discount: int
    amount: int

    class Config:
        extra = "allow"


class InvoiceData(BaseModel):
    root: Dict[str, InvoiceItem]

    class Config:
        from_attributes = True
