from uuid import UUID

from pydantic import BaseModel, ConfigDict


class SearchResult(BaseModel):
    id: UUID
    document_id: UUID
    chunk_index: int
    content: str

    model_config = ConfigDict(from_attributes=True)