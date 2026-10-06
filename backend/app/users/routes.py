from fastapi import APIRouter, Depends

from app.auth.models import User
from app.auth.schemas import UserResponse
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user