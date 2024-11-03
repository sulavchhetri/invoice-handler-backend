from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from src.schemas import InvoiceData
from src.database import get_db
from src.crud import create_invoice, get_all_invoices
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
