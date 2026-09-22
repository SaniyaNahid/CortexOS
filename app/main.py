from fastapi import FastAPI

from app.auth.routes import router as auth_router
from app.organizations.routes import router as organization_router
from app.workspaces.routes import router as workspace_router
from app.documents.routes import router as document_router
from app.document_chunks.routes import router as document_chunk_router


app = FastAPI(
    title="CortexOS",
    description="AI-Powered Enterprise Intelligence and Decision Support System",
    version="1.0.0",
)


app.include_router(auth_router)
app.include_router(organization_router)
app.include_router(workspace_router)
app.include_router(document_router)
app.include_router(document_chunk_router)


@app.get("/")
def root():
    return {
        "message": "CortexOS API is running"
    }