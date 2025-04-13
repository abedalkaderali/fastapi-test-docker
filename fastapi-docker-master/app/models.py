from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.core.database import Base


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    balance = Column(Float, default=0.0)
    transactions = relationship("Transaction", back_populates="account")

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    amount = Column(Integer, nullable=False)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    account = relationship("Account", back_populates="transactions")
    timestamp = Column(String, nullable=False, default=str(datetime.now()))
    transaction_type = Column(String, nullable=False)