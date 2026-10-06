from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.organizations.routes import router as organization_router
from app.workspaces.routes import router as workspace_router
from app.documents.routes import router as document_router
from app.document_chunks.routes import router as document_chunk_router
from app.search.routes import router as search_router


app = FastAPI(
    title="CortexOS",
    description="AI-Powered Enterprise Intelligence and Decision Support System",
    version="1.0.0",
)


# Authentication
app.include_router(auth_router)

# Organizations
app.include_router(organization_router)

# Workspaces
app.include_router(workspace_router)

# Documents
app.include_router(document_router)

# Document Chunks
app.include_router(document_chunk_router)

# Semantic Search
app.include_router(search_router)


@app.get("/")
def root():
    return {
        "message": "CortexOS API is running"
    }