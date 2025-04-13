from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import accounts, transactions

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI RESTful API for accounts and transactions."}