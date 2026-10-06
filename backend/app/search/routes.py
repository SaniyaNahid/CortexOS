from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies.auth import get_current_user
from app.search.schemas import SearchResult
from app.search.service import SearchService


router = APIRouter(
    prefix="/search",
    tags=["Semantic Search"]
)


@router.get("", response_model=list[SearchResult])
def semantic_search(
    query: str,
    limit: int = 5,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        return SearchService.search(
            db,
            query,
            limit
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )