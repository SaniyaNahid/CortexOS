from uuid import UUID

from sqlalchemy.orm import Session

from app.organizations.repository import OrganizationRepository
from app.workspaces.models import Workspace
from app.workspaces.repository import WorkspaceRepository
from app.workspaces.schemas import WorkspaceCreate


class WorkspaceService:

    @staticmethod
    def create_workspace(
        db: Session,
        workspace_data: WorkspaceCreate,
        current_user,
    ):
        organization = OrganizationRepository.get_by_id(
            db,
            workspace_data.organization_id,
        )

        if organization is None:
            raise ValueError("Organization not found.")

        if organization.owner_id != current_user.id:
            raise ValueError(
                "You are not the owner of this organization."
            )

        workspace = Workspace(
            name=workspace_data.name,
            description=workspace_data.description,
            organization_id=workspace_data.organization_id,
        )

        return WorkspaceRepository.create(
            db,
            workspace,
        )

    @staticmethod
    def get_workspaces(
        db: Session,
        organization_id: UUID,
    ):
        return WorkspaceRepository.get_by_organization(
            db,
            organization_id,
        )