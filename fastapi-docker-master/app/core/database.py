from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
# Set up the database URL and engine            
# You can replace this with your actual database URL
# and engine configuration
# Example: PostgreSQL   # DATABASE_URL = "postgresql://user:password@localhost/dbname"

DATABASE_URL = os.getenv("DATABASE_URL")  # Default to SQLite if not set

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()