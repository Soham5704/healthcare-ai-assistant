from langchain_community.llms import Ollama
from .config import OLLAMA_MODEL

def get_llm():
    """Initializes and returns the local Ollama LLM."""
    print(f"Loading local LLM: {OLLAMA_MODEL}...")
    llm = Ollama(model=OLLAMA_MODEL)
    return llm