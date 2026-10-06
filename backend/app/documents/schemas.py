from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DocumentResponse(BaseModel):
    id: UUID
    title: str
    filename: str
    file_path: str
    file_type: str
    file_size: int
    extracted_text: str | None
    workspace_id: UUID
    uploaded_by: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)