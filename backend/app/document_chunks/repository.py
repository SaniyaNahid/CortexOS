from uuid import UUID

from sqlalchemy.orm import Session

from app.document_chunks.models import DocumentChunk


class DocumentChunkRepository:

    @staticmethod
    def create(
        db: Session,
        chunk: DocumentChunk
    ) -> DocumentChunk:
        db.add(chunk)
        db.commit()
        db.refresh(chunk)
        return chunk

    @staticmethod
    def create_many(
        db: Session,
        chunks: list[DocumentChunk]
    ) -> list[DocumentChunk]:
        db.add_all(chunks)
        db.commit()

        for chunk in chunks:
            db.refresh(chunk)

        return chunks

    @staticmethod
    def get_by_id(
        db: Session,
        chunk_id: UUID
    ) -> DocumentChunk | None:
        return (
            db.query(DocumentChunk)
            .filter(DocumentChunk.id == chunk_id)
            .first()
        )

    @staticmethod
    def get_by_document(
        db: Session,
        document_id: UUID
    ) -> list[DocumentChunk]:
        return (
            db.query(DocumentChunk)
            .filter(DocumentChunk.document_id == document_id)
            .order_by(DocumentChunk.chunk_index)
            .all()
        )

    @staticmethod
    def update_embedding(
        db: Session,
        chunk: DocumentChunk,
        embedding: list[float]
    ) -> DocumentChunk:
        chunk.embedding = embedding

        db.commit()
        db.refresh(chunk)

        return chunk