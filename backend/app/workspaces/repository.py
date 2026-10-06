from uuid import UUID

from sqlalchemy.orm import Session

from app.workspaces.models import Workspace


class WorkspaceRepository:

    @staticmethod
    def create(db: Session, workspace: Workspace) -> Workspace:
        db.add(workspace)
        db.commit()
        db.refresh(workspace)
        return workspace

    @staticmethod
    def get_by_id(
        db: Session,
        workspace_id: UUID,
    ) -> Workspace | None:
        return (
            db.query(Workspace)
            .filter(Workspace.id == workspace_id)
            .first()
        )

    @staticmethod
    def get_by_organization(
        db: Session,
        organization_id: UUID,
    ) -> list[Workspace]:
        return (
            db.query(Workspace)
            .filter(Workspace.organization_id == organization_id)
            .all()
        )