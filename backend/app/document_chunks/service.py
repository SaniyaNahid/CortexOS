from uuid import UUID

from sqlalchemy.orm import Session

from app.document_chunks.repository import DocumentChunkRepository
from app.processing.embedding import generate_embedding


class DocumentChunkService:

    @staticmethod
    def generate_chunk_embedding(
        db: Session,
        chunk_id: UUID
    ):
        chunk = DocumentChunkRepository.get_by_id(
            db,
            chunk_id
        )

        if chunk is None:
            raise ValueError("Document chunk not found.")

        embedding = generate_embedding(
            chunk.content
        )

        return DocumentChunkRepository.update_embedding(
            db,
            chunk,
            embedding
        )