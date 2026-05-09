import os

# Define the paths for our data and vector database
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
VECTOR_STORE_DIR = os.path.join(BASE_DIR, "vector_store")

# LLM Configuration
OLLAMA_MODEL = "llama3" 
EMBEDDING_MODEL = "all-MiniLM-L6-v2"