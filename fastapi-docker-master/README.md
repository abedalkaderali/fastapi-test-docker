# FastAPI REST API

This project implements a RESTful API for handling basic operations for accounts and transactions using FastAPI. The API supports creating and updating accounts, creating transactions, and retrieving all transactions. Data is stored in either MySQL or PostgreSQL.

## Project Structure

```
fastapi-rest-api
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── accounts.py
│   │   └── transactions.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   ├── models.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── account.py
│   │   └── transaction.py
│   └── tests
│       ├── __init__.py
│       ├── test_accounts.py
│       └── test_transactions.py
├── requirements.txt
├── alembic.ini
├── README.md
└── .env
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-rest-api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your database connection in the `.env` file.

## Running the Application

To run the FastAPI application, execute the following command:
```
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Running Alembic Migrations

Before running the application or tests, ensure the database schema is up to date by running Alembic migrations:

1. Generate a new migration (if needed):
   ```
   alembic revision --autogenerate -m "Initial migration"
   ```

2. Apply the migrations:
   ```
   alembic upgrade head
   ```

This will create the necessary tables in your database.

## API Endpoints

### Accounts

- **Create an Account**
  - `POST /accounts/`
  
- **Update an Account**
  - `PUT /accounts/{account_id}`

### Transactions

- **Create a Transaction**
  - `POST /transactions/`
  
- **Retrieve All Transactions**
  - `GET /transactions/`

## Testing

To run the unit tests, follow these steps:

1. Ensure the database is set up and migrations are applied:
   ```
   alembic upgrade head
   ```

2. Run the tests:
   ```
   pytest app/tests
   ```

## Documentation

Automatic API documentation is available at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## License

This project is licensed under the MIT License.