from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.models import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=TransactionResponse, status_code=201)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return TransactionResponse.model_validate(db_transaction)

@router.get("/", response_model=list[TransactionResponse], status_code=200)
def get_transactions(account_id: Optional[int] = Query(None), db: Session = Depends(get_db)):
    if account_id:
        transactions = db.query(Transaction).filter(Transaction.account_id == account_id).all()
    else:
        transactions = db.query(Transaction).all()
    return [TransactionResponse.model_validate(t) for t in transactions]