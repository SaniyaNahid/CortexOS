from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="CortexOS API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CortexOS API",
        "database": settings.DATABASE_NAME,
    }