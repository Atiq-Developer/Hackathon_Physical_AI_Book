from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Filter
from typing import List

# Load same embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Qdrant local DB
qdrant = QdrantClient(path="app/rag/qdrant")

COLLECTION = "physical_ai_book"

def search_chunks(query: str, limit: int = 5):
    query_vector = model.encode(query).tolist()

    hits = qdrant.search(
        collection_name=COLLECTION,
        query_vector=query_vector,
        limit=limit
    )

    return [hit.payload["content"] for hit in hits]


def build_context(chunks: List[str]) -> str:
    return "\n\n".join(chunks)
