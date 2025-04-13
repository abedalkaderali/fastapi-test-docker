from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional
from datetime import datetime

class TransactionBase(BaseModel):
    account_id: int
    amount: float
    transaction_type: Literal["Deposit", "withdrawal"] = "Deposit"
    timestamp: Optional[datetime]
    

class TransactionCreate(TransactionBase):
    account_id: int
    amount: float
    transaction_type: Optional[Literal["Deposit", "withdrawal"]] = "Deposit"

class Transaction(TransactionBase):
    id: int
    timestamp: Optional[datetime]

    class Config:
        from_attributes = True

class TransactionResponse(BaseModel):
    id: int
    account_id: int
    amount: float
    timestamp: Optional[str]
    transaction_type: Optional[Literal["Deposit", "withdrawal"]]

    class Config:
        from_attributes = True