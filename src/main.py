from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.invoice import router as invoice_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://invoice-handler.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)


app.include_router(invoice_router)
