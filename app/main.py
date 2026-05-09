from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .rag import setup_rag_pipeline
from .agent import process_query

# Initialize the FastAPI app
app = FastAPI(
    title="Healthcare AI Assistant API",
    description="A RAG-based AI assistant for healthcare documents.",
    version="1.0.0"
)

# Allow cross-origin requests so your local frontend HTML file can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected format for incoming questions
class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    """Assignment Requirement: GET /health"""
    return {"status": "healthy", "message": "API is running smoothly."}

@app.post("/ingest")
def ingest_documents():
    """Assignment Requirement: POST /ingest"""
    try:
        setup_rag_pipeline()
        return {"message": "Documents successfully ingested into the vector database."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask")
def ask(request: QuestionRequest):
    """Assignment Requirement: POST /ask"""
    try:
        response = process_query(request.question)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))