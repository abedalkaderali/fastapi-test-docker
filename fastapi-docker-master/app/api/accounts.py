from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Account
from app.schemas.account import AccountCreate, AccountUpdate, AccountResponse
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=AccountResponse, status_code=201)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return AccountResponse.model_validate(db_account)

@router.put("/{account_id}", response_model=AccountResponse, status_code=200)
def update_account(account: AccountUpdate, db: Session = Depends(get_db)):
    db_account = db.query(Account).filter(Account.id == account.id).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")

    if not account.model_dump(exclude_unset=True):
        raise HTTPException(status_code=400, detail="No valid fields provided for update")

    for key, value in account.model_dump(exclude_unset=True).items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return AccountResponse.model_validate(db_account)

@router.get("/", response_model=list[AccountResponse], status_code=200)
def get_accounts(db: Session = Depends(get_db)):
    accounts = db.query(Account).all()
    return [AccountResponse.model_validate(account) for account in accounts]