from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.database.connection import engine
from app.database.base import Base

app = FastAPI(
    title="CortexOS API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to CortexOS API"
    }