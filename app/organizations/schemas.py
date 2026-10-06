from uuid import UUID

from pydantic import BaseModel, ConfigDict


class OrganizationCreate(BaseModel):
    name: str
    description: str | None = None


class OrganizationUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class OrganizationResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    owner_id: UUID

    model_config = ConfigDict(from_attributes=True)