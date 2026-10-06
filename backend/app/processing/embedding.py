from google import genai

from app.core.config import settings


EMBEDDING_MODEL = "gemini-embedding-2-preview"


def generate_embedding(text: str) -> list[float]:
    if not text or not text.strip():
        raise ValueError("Text cannot be empty.")

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
    )

    return result.embeddings[0].values