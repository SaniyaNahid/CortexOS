import os
import shutil
import uuid

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.documents.models import Document
from app.documents.repository import DocumentRepository
from app.processing.extractor import extract_text_from_pdf
from app.processing.chunker import chunk_text
from app.document_chunks.models import DocumentChunk
from app.document_chunks.repository import DocumentChunkRepository
from app.workspaces.repository import WorkspaceRepository


UPLOAD_DIR = "uploads"


class DocumentService:

    @staticmethod
    def upload_document(
        db: Session,
        workspace_id,
        current_user,
        file: UploadFile,
    ):
        workspace = WorkspaceRepository.get_by_id(
            db,
            workspace_id,
        )

        if workspace is None:
            raise ValueError("Workspace not found.")

        os.makedirs(UPLOAD_DIR, exist_ok=True)

        filename = f"{uuid.uuid4()}_{file.filename}"

        file_path = os.path.join(
            UPLOAD_DIR,
            filename,
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        extracted_text = None

        if file.content_type == "application/pdf":
            extracted_text = extract_text_from_pdf(file_path)

        document = Document(
            title=file.filename,
            filename=filename,
            file_path=file_path,
            file_type=file.content_type,
            file_size=os.path.getsize(file_path),
            extracted_text=extracted_text,
            workspace_id=workspace_id,
            uploaded_by=current_user.id,
        )

        document = DocumentRepository.create(
            db,
            document,
        )

        # Create chunks from extracted text
        if extracted_text:
            text_chunks = chunk_text(extracted_text)

            chunk_objects = []

            for index, content in enumerate(text_chunks):
                chunk = DocumentChunk(
                    document_id=document.id,
                    chunk_index=index,
                    content=content,
                )

                chunk_objects.append(chunk)

            if chunk_objects:
                DocumentChunkRepository.create_many(
                    db,
                    chunk_objects,
                )

        return document

    @staticmethod
    def get_documents(
        db: Session,
        workspace_id,
    ):
        return DocumentRepository.get_by_workspace(
            db,
            workspace_id,
        )