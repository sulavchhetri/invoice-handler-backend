from typing import Dict
from pydantic import BaseModel


class InvoiceItem(BaseModel):
    task: str
    hours: int
    unit_price: int
    discount: int
    amount: int

class InvoiceData(BaseModel):
    root: Dict[str, InvoiceItem]

    class Config:
        from_attributes = True
