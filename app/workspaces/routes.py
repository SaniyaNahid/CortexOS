from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies.auth import get_current_user
from app.workspaces.schemas import (
    WorkspaceCreate,
    WorkspaceResponse,
)
from app.workspaces.service import WorkspaceService

router = APIRouter(
    prefix="/workspaces",
    tags=["Workspaces"],
)


@router.post(
    "",
    response_model=WorkspaceResponse,
)
def create_workspace(
    workspace: WorkspaceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    try:
        return WorkspaceService.create_workspace(
            db,
            workspace,
            current_user,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/{organization_id}",
    response_model=list[WorkspaceResponse],
)
def get_workspaces(
    organization_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return WorkspaceService.get_workspaces(
        db,
        organization_id,
    )