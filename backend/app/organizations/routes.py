from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.auth.models import User
from app.database.connection import get_db
from app.dependencies.auth import get_current_user
from app.organizations.schemas import (
    OrganizationCreate,
    OrganizationResponse,
)
from app.organizations.service import OrganizationService

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"],
)


@router.post(
    "",
    response_model=OrganizationResponse,
)
def create_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return OrganizationService.create_organization(
        db,
        current_user,
        organization,
    )


@router.get(
    "/me",
    response_model=list[OrganizationResponse],
)
def get_my_organizations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return OrganizationService.get_my_organizations(
        db,
        current_user,
    )