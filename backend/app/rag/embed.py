import json
from pathlib import Path
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

# Load local embedding model (FREE)
model = SentenceTransformer("all-MiniLM-L6-v2")  # 384 dims

BASE_DIR = Path(__file__).resolve().parent
CHUNKS_FILE = BASE_DIR / "chunks.json"

# Local Qdrant (file-based, Vercel-safe)
qdrant = QdrantClient(path=BASE_DIR / "qdrant")

COLLECTION = "physical_ai_book"

def embed_text(text: str):
    return model.encode(text).tolist()

def main():
    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    # Recreate collection
    qdrant.recreate_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        ),
    )

    points = []
    for i, chunk in enumerate(chunks):
        vector = embed_text(chunk["content"])
        points.append(
            PointStruct(
                id=i,
                vector=vector,
                payload={
                    "source": chunk["source"],
                    "content": chunk["content"]
                }
            )
        )

    qdrant.upsert(collection_name=COLLECTION, points=points)
    print(f"✅ Embedded {len(points)} chunks into Qdrant (LOCAL MODEL)")

if __name__ == "__main__":
    main()
