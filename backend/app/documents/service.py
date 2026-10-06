import os
import shutil
import uuid

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.documents.models import Document
from app.documents.repository import DocumentRepository
from app.processing.extractor import extract_text_from_pdf
from app.processing.chunker import chunk_text
from app.processing.embedding import generate_embedding
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
        file: UploadFile
    ):

        # 1. Verify workspace
        workspace = WorkspaceRepository.get_by_id(
            db,
            workspace_id
        )

        if workspace is None:
            raise ValueError("Workspace not found.")

        # 2. Create upload directory
        os.makedirs(
            UPLOAD_DIR,
            exist_ok=True
        )

        # 3. Generate unique filename
        filename = f"{uuid.uuid4()}_{file.filename}"

        file_path = os.path.join(
            UPLOAD_DIR,
            filename
        )

        # 4. Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer
            )

        # 5. Extract text
        extracted_text = None

        if file.content_type == "application/pdf":

            extracted_text = extract_text_from_pdf(
                file_path
            )

        # 6. Create document record
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
            document
        )

        # 7. Create chunks
        if extracted_text:

            text_chunks = chunk_text(
                extracted_text
            )

            chunk_objects = []

            for index, content in enumerate(text_chunks):

                chunk = DocumentChunk(
                    document_id=document.id,
                    chunk_index=index,
                    content=content,
                )

                chunk_objects.append(chunk)

            # 8. Save chunks
            if chunk_objects:

                DocumentChunkRepository.create_many(
                    db,
                    chunk_objects
                )

                # 9. Generate embeddings
                for chunk in chunk_objects:

                    embedding = generate_embedding(
                        chunk.content
                    )

                    # 10. Save embedding
                    DocumentChunkRepository.update_embedding(
                        db,
                        chunk,
                        embedding
                    )

        return document

    @staticmethod
    def get_documents(
        db: Session,
        workspace_id
    ):

        return DocumentRepository.get_by_workspace(
            db,
            workspace_id
        )