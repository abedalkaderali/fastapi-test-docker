from fastapi.testclient import TestClient
from app.main import app
from app.models import Account
from app.schemas.account import AccountCreate, AccountUpdate
from app.core.database import get_db
from sqlalchemy.orm import Session

client = TestClient(app)

def override_get_db():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

def test_create_account():
    account_data = {"name": "Test Account", "email":"ib@mail.com", "balance": 100.0}
    response = client.post("/accounts/", json=account_data)
    assert response.status_code == 201
    assert response.json()["name"] == account_data["name"]
    assert response.json()["balance"] == account_data["balance"]

def test_update_account():
    account_data = {"id":"1","name": "Updated Account", "balance": 100.0}
    create_account_data = {"name": "Test Account", "email":"ib@mail.com", "balance": 100.0}

    # First create an account to update
    create_response = client.post("/accounts/", json=create_account_data)
    account_id = create_response.json()["id"]
    
    update_response = client.put(f"/accounts/{account_id}", json=account_data)
    assert update_response.status_code == 200
    assert update_response.json()["name"] == account_data["name"]
    assert update_response.json()["balance"] == account_data["balance"]