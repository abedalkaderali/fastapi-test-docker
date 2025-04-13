from datetime import datetime
from fastapi.testclient import TestClient
from app.main import app
from app.models import Transaction
from app.schemas.transaction import TransactionCreate
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.core.database import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    Base.metadata.create_all(bind=engine)  # Create tables in the test database
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def setup_function():
    """Reset the database before each test."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_create_transaction():
    transaction_data = {
        "amount": 100.0,
        "account_id": 1,
        "transaction_type": "Deposit",
        "timestamp": str(datetime.now())
    }
    response = client.post("/transactions/", json=transaction_data)
    assert response.status_code == 201
    assert response.json()["amount"] == transaction_data["amount"]
    assert response.json()["account_id"] == transaction_data["account_id"]
    assert response.json()["transaction_type"] == transaction_data["transaction_type"]
    assert response.status_code == 201
    assert response.json()["amount"] == 100.0
    assert response.json()["account_id"] == 1

def test_get_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_transaction_missing_fields():
    response = client.post("/transactions/", json={"amount": 100.0})
    assert response.status_code == 422  # Unprocessable Entity due to missing account_id

def test_get_transactions_empty():
    response = client.get("/transactions/")
    assert response.status_code == 200
    assert response.json() == []  # Assuming no transactions exist initially