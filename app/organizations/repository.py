from uuid import UUID

from sqlalchemy.orm import Session

from app.organizations.models import Organization


class OrganizationRepository:

    @staticmethod
    def create(
        db: Session,
        organization: Organization,
    ) -> Organization:
        db.add(organization)
        db.commit()
        db.refresh(organization)
        return organization

    @staticmethod
    def get_by_id(
        db: Session,
        organization_id: UUID,
    ) -> Organization | None:
        return (
            db.query(Organization)
            .filter(Organization.id == organization_id)
            .first()
        )

    @staticmethod
    def get_by_owner(
        db: Session,
        owner_id: UUID,
    ) -> list[Organization]:
        return (
            db.query(Organization)
            .filter(Organization.owner_id == owner_id)
            .all()
        )