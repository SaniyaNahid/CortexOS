from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.schemas import UserRegister, UserResponse
from app.auth.service import AuthService
from app.database.connection import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register", response_model=UserResponse)
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    try:
        return AuthService.register_user(db, user)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )