import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from .llm import get_llm
from .config import DATA_DIR, VECTOR_STORE_DIR, EMBEDDING_MODEL

# Initialize the embedding model (converts text to numbers)
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def setup_rag_pipeline():
    """Reads documents, creates chunks, and saves to ChromaDB."""
    print("Starting document ingestion...")
    
    # 1. Load documents from the data folder
    loader = DirectoryLoader(DATA_DIR, glob="**/*.txt", loader_cls=TextLoader)
    documents = loader.load()
    
    if not documents:
        print("No documents found in the data directory!")
        return

    # 2. Split into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    
    # 3. Store in ChromaDB vector database
    print(f"Storing {len(chunks)} chunks in ChromaDB...")
    Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=VECTOR_STORE_DIR
    )
    print("Ingestion complete!")

def ask_question(question: str):
    """Searches the database and asks the LLM to generate an answer."""
    vectorstore = Chroma(persist_directory=VECTOR_STORE_DIR, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    llm = get_llm()
    
    docs = retriever.invoke(question)
    
    if not docs:
        return {"answer": "I could not find this information in the provided documents.", "sources": []}
    
    context = "\n\n".join([doc.page_content for doc in docs])
    sources = [{"document": os.path.basename(doc.metadata.get('source', 'Unknown')), "chunk": doc.page_content[:100] + "..."} for doc in docs]
    
    prompt_template = """
    You are a professional healthcare AI assistant. Answer the user's question based ONLY on the following context.
    If the answer is not in the context, you must clearly state: "I could not find this information in the provided documents."
    Do not guess, do not hallucinate, and do not provide direct medical advice.
    
    Context:
    {context}
    
    Question: {question}
    Answer:
    """
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    final_prompt = prompt.format(context=context, question=question)
    
    print("Generating answer...")
    answer = llm.invoke(final_prompt)
    
    return {"answer": answer.strip(), "sources": sources}