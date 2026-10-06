import uuid

from sqlalchemy.orm import Session

from app.auth.models import User
from app.organizations.models import Organization
from app.organizations.repository import OrganizationRepository
from app.organizations.schemas import OrganizationCreate


class OrganizationService:

    @staticmethod
    def create_organization(
        db: Session,
        current_user: User,
        organization_data: OrganizationCreate,
    ):
        organization = Organization(
            id=uuid.uuid4(),
            name=organization_data.name,
            description=organization_data.description,
            owner_id=current_user.id,
        )

        return OrganizationRepository.create(
            db,
            organization,
        )

    @staticmethod
    def get_my_organizations(
        db: Session,
        current_user: User,
    ):
        return OrganizationRepository.get_by_owner(
            db,
            current_user.id,
        )