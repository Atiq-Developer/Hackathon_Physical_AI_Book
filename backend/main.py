from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Physical AI RAG API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "✅ Physical AI Backend is LIVE!", "status": "deployed"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: dict):
    return {
        "question": request.get("question", ""),
        "answer": "🎉 Backend deployed successfully! Full RAG functionality coming soon with Qdrant Cloud."
    }