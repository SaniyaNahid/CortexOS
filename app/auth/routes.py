from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.schemas import (
    UserRegister,
    UserResponse,
    Token,
)
from app.auth.service import AuthService
from app.database.connection import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    try:
        return AuthService.register_user(
            db,
            user,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=Token,
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    try:
        return AuthService.login_user(
            db,
            form_data.username,   # Email is passed in the username field
            form_data.password,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )