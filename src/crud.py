"""
    
"""

from sqlalchemy.orm import Session
from src.models import Invoice
from src.utils.util import format_invoices


def create_invoice(
    db: Session,
    task_id: str,
    task: str,
    hours: int,
    unitprice: int,
    discount: int,
    amount: int,
):
    db_invoice = Invoice(
        task_id=task_id,
        task=task,
        hours=hours,
        unitprice=unitprice,
        discount=discount,
        amount=amount,
    )
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice


def get_all_invoices(db: Session):
    invoices = db.query(Invoice).all()
    invoice_dicts = [invoice.__dict__ for invoice in invoices]
    formatted_invoices = format_invoices(invoice_dicts)
    return formatted_invoices
