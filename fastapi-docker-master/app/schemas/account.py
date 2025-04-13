from pydantic import BaseModel
from typing import Optional

class AccountCreate(BaseModel):
    name: str
    email: str
    balance: Optional[float] = 0.0

class AccountUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None

class AccountResponse(BaseModel):
    id: int
    name: str
    balance: float
    email: Optional[str]

    class Config:
        from_attributes = True