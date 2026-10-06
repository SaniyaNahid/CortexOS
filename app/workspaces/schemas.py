from uuid import UUID

from pydantic import BaseModel, ConfigDict


class WorkspaceCreate(BaseModel):
    name: str
    description: str | None = None
    organization_id: UUID


class WorkspaceResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    organization_id: UUID

    model_config = ConfigDict(from_attributes=True)