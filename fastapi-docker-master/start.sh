#!/bin/bash
export PYTHONPATH=/app

echo "🔄 Waiting for PostgreSQL to be ready..."

while ! nc -z db 5432; do
  sleep 1
done

echo "✅ PostgreSQL is up - running Alembic migrations..."


alembic upgrade head

echo "🚀 Starting FastAPI..."

exec uvicorn app.main:app --host 0.0.0.0 --port 8000

