from .rag import ask_question

def check_available_slots(department: str = "General", date: str = "soon"):
    """Mock tool for checking appointment slots."""
    return {
        "answer": f"I can check mock appointment availability. Available slots for {department} are Monday at 10:00 AM and Tuesday at 2:00 PM.",
        "sources": []
    }

def process_query(question: str):
    """
    Agentic Router:
    Decides whether to use the RAG pipeline or a specific tool based on the user's intent.
    """
    question_lower = question.lower()
    
    # Simple keyword-based routing (Agentic Workflow)
    if "appointment" in question_lower or "book" in question_lower or "schedule" in question_lower:
        print("Agent routing to: Appointment Tool")
        return check_available_slots()
    else:
        print("Agent routing to: RAG Knowledge Base")
        return ask_question(question)