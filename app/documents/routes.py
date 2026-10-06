from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.dependencies.auth import get_current_user
from app.documents.schemas import DocumentResponse
from app.documents.service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "/upload",
    response_model=DocumentResponse,
)
def upload_document(
    workspace_id: UUID = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    try:
        return DocumentService.upload_document(
            db=db,
            workspace_id=workspace_id,
            current_user=current_user,
            file=file,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/{workspace_id}",
    response_model=list[DocumentResponse],
)
def get_documents(
    workspace_id: UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return DocumentService.get_documents(
        db,
        workspace_id,
    )