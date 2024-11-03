from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas import InvoiceItem
from src.database import get_db
from src.crud import (
    create_invoice,
    get_all_invoices,
    delete_invoice_by_task_id,
    update_invoice_by_task_id,
)
from src.utils.util import get_extra_keys
from typing import Dict

router = APIRouter()


@router.post("/invoices/")
async def save_invoices(request_data: Dict, db: Session = Depends(get_db)):
    try:

        def save_invoice(key, item):
            create_invoice(
                db,
                key,
                item["task"],
                item["hours"],
                item["unit_price"],
                item["discount"],
                item["amount"],
            )
            extra_keys = get_extra_keys(item)
            for extra_key in extra_keys:
                nested_item = item[extra_key]
                save_invoice(extra_key, nested_item)

        for key, item in request_data.items():
            save_invoice(key, item)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Invoices created successfully."}


@router.get("/invoices/")
async def get_invoices(db: Session = Depends(get_db)):
    return get_all_invoices(db)


@router.delete("/invoices/{task_id}")
async def delete_invoice(task_id: str, db: Session = Depends(get_db)):
    try:
        result = delete_invoice_by_task_id(db, task_id)
        if not result:
            raise HTTPException(status_code=404, detail="Invoice not found")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Invoice deleted successfully."}


@router.post("/invoices/{task_id}")
async def save_invoice(
    task_id: str, request_data: InvoiceItem, db: Session = Depends(get_db)
):
    try:
        create_invoice(
            db,
            task_id,
            request_data.task,
            request_data.hours,
            request_data.unit_price,
            request_data.discount,
            request_data.amount,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Invoice created successfully."}


@router.put("/invoices/{task_id}")
async def update_invoice_endpoint(
    task_id: str, request_data: InvoiceItem, db: Session = Depends(get_db)
):
    try:
        updated_invoice = update_invoice_by_task_id(db, task_id, request_data)
        if not updated_invoice:
            raise HTTPException(status_code=404, detail="Invoice not found.")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Invoice updated successfully."}
