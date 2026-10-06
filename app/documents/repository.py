from uuid import UUID

from sqlalchemy.orm import Session

from app.documents.models import Document


class DocumentRepository:

    @staticmethod
    def create(
        db: Session,
        document: Document,
    ) -> Document:
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def get_by_workspace(
        db: Session,
        workspace_id: UUID,
    ) -> list[Document]:
        return (
            db.query(Document)
            .filter(Document.workspace_id == workspace_id)
            .all()
        )