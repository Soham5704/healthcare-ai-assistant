# Mindbowser Healthcare AI Assistant

A prototype Healthcare AI Assistant built using FastAPI, LangChain, ChromaDB, and a local Llama 3 model (via Ollama). This application uses a Retrieval-Augmented Generation (RAG) pipeline to answer questions based on a provided synthetic telehealth policy.

## Architecture & Technical Choices
* **Framework:** FastAPI for robust, asynchronous API endpoints.
* **LLM:** `llama3` (Local via Ollama) to ensure zero data leakage and maintain complete patient privacy.
* **Embeddings:** `all-MiniLM-L6-v2` via HuggingFace for fast, local text vectorization.
* **Vector Database:** ChromaDB for local semantic search and document retrieval.
* **Agentic Routing:** A custom logic router (`agent.py`) intercepts appointment-related queries and routes them to a mock scheduling tool, bypassing the RAG pipeline.

## Prompt Engineering Strategy
To prevent hallucination and ensure strict adherence to the provided documents, the following prompt template was utilized:

> You are a professional healthcare AI assistant. Answer the user's question based ONLY on the following context.
> If the answer is not in the context, you must clearly state: "I could not find this information in the provided documents."
> Do not guess, do not hallucinate, and do not provide direct medical advice.

## Setup & Run Instructions

**1. Prerequisites**
* Python 3.10+
* [Ollama](https://ollama.com/) installed and running locally.
* Download the model: `ollama run llama3`

**2. Local Installation**
```bash
python -m venv venv
venv\Scripts\activate  # On Mac/Linux use: source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload