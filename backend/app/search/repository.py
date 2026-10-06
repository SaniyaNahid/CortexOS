from sqlalchemy.orm import Session

from app.document_chunks.models import DocumentChunk


class SearchRepository:

    @staticmethod
    def semantic_search(
        db: Session,
        query_embedding: list[float],
        limit: int = 5
    ) -> list[DocumentChunk]:

        results = (
            db.query(DocumentChunk)
            .filter(DocumentChunk.embedding.is_not(None))
            .order_by(
                DocumentChunk.embedding.cosine_distance(query_embedding)
            )
            .limit(limit)
            .all()
        )

        return results