from fastapi import FastAPI
from src.routes.invoice import router as invoice_router

app = FastAPI()


app.include_router(invoice_router)
