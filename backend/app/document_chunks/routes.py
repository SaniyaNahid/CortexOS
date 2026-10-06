from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies.auth import get_current_user
from app.document_chunks.repository import DocumentChunkRepository
from app.document_chunks.schemas import DocumentChunkResponse


router = APIRouter(
    prefix="/document-chunks",
    tags=["Document Chunks"],
)


@router.get(
    "/{document_id}",
    response_model=list[DocumentChunkResponse],
)
def get_document_chunks(
    document_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return DocumentChunkRepository.get_by_document(
        db,
        document_id,
    )