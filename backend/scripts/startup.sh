#!/bin/sh

echo "Running Alembic migrations..."
alembic upgrade head

echo "Starting FastAPI application..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8080 --loop asyncio