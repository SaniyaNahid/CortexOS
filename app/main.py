from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.database.connection import engine

app = FastAPI(
    title="CortexOS API",
    version="1.0.0",
)


@app.on_event("startup")
def startup():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("✅ Database connected successfully!")


@app.get("/")
def root():
    return {
        "message": "Welcome to CortexOS API",
        "database": settings.DATABASE_NAME,
    }