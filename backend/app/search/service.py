from sqlalchemy.orm import Session

from app.processing.embedding import generate_embedding
from app.search.repository import SearchRepository


class SearchService:

    @staticmethod
    def search(
        db: Session,
        query: str,
        limit: int = 5
    ):

        if not query or not query.strip():
            raise ValueError("Search query cannot be empty.")

        # 1. Convert user's query into an embedding
        query_embedding = generate_embedding(query)

        # 2. Search the database using vector similarity
        results = SearchRepository.semantic_search(
            db,
            query_embedding,
            limit
        )

        return results