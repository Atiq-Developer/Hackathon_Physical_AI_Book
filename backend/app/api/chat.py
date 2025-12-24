from fastapi import APIRouter
from pydantic import BaseModel
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import os

router = APIRouter()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Qdrant Client - with fallback
COLLECTION = "physical_ai_book"

try:
    # Try local path first (for development)
    if os.path.exists("app/rag/qdrant"):
        qdrant = QdrantClient(path="app/rag/qdrant")
    else:
        # Production: Use Qdrant Cloud (set environment variables)
        qdrant_url = os.getenv("QDRANT_URL")
        qdrant_key = os.getenv("QDRANT_API_KEY")
        
        if qdrant_url and qdrant_key:
            qdrant = QdrantClient(url=qdrant_url, api_key=qdrant_key)
        else:
            qdrant = None  # No Qdrant available
except Exception as e:
    print(f"Qdrant initialization error: {e}")
    qdrant = None

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(req: ChatRequest):
    # Check if Qdrant is available
    if qdrant is None:
        return {
            "question": req.question,
            "answer": "✅ Backend deployed successfully! 🎉\n\n⚠️ Note: Qdrant database setup is pending. Please configure Qdrant Cloud for full functionality.\n\nYour question: " + req.question
        }
    
    try:
        query_vector = model.encode(req.question).tolist()

        search_results = qdrant.query_points(
            collection_name=COLLECTION,
            query=query_vector,
            limit=2
        ).points

        # Extract and combine context
        context = "\n\n".join([hit.payload["content"] for hit in search_results])
        
        # Truncate for concise answer
        max_length = 600
        if len(context) > max_length:
            truncated = context[:max_length]
            last_period = truncated.rfind('.')
            if last_period > 0:
                context = truncated[:last_period + 1]
            else:
                context = truncated + "..."
        
        answer = f"""📚 Based on Physical AI Book:

{context}

💡 Want more details? Ask a more specific question!"""

        return {
            "question": req.question,
            "answer": answer
        }
    
    except Exception as e:
        return {
            "question": req.question,
            "answer": f"⚠️ Error occurred: {str(e)}\n\nBackend is running but Qdrant needs configuration."
        }