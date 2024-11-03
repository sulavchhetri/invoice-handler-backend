"""
    This module is used to perform CRUD operation on the database.
"""

from sqlalchemy.orm import Session
from src.models import Invoice
from src.utils.util import format_invoices
from src.schemas import InvoiceItem


def create_invoice(
    db: Session,
    task_id: str,
    task: str,
    hours: int,
    unit_price: int,
    discount: int,
    amount: int,
):
    db_invoice = Invoice(
        task_id=task_id,
        task=task,
        hours=hours,
        unit_price=unit_price,
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


def delete_invoice_by_task_id(db: Session, task_id: str):
    invoice = db.query(Invoice).filter(Invoice.task_id == task_id).first()
    if invoice:
        db.delete(invoice)
        db.commit()
        return True
    return False


def update_invoice_by_task_id(db: Session, task_id: str, request_data: InvoiceItem):
    invoice = db.query(Invoice).filter(Invoice.task_id == task_id).first()

    if not invoice:
        return None

    invoice.task = request_data.task
    invoice.hours = request_data.hours
    invoice.unit_price = request_data.unit_price
    invoice.discount = request_data.discount
    invoice.amount = request_data.amount
    db.commit()
    return invoice
