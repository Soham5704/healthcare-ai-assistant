from .rag import ask_question

def check_available_slots(question: str):
    """Mock tool that actually reads the requested day."""
    question_lower = question.lower()
    
    # Check what day the user is asking for
    if "monday" in question_lower:
        answer = "Yes! We have an available slot on Monday at 10:00 AM. I have successfully booked that for you."
    elif "tuesday" in question_lower:
        answer = "Yes! We have an available slot on Tuesday at 2:00 PM. I have successfully booked that for you."
    elif "wednesday" in question_lower or "thursday" in question_lower or "friday" in question_lower:
        answer = "I'm sorry, we are completely booked on that day. Our only available slots are Monday at 10:00 AM and Tuesday at 2:00 PM."
    else:
        answer = "I can check mock appointment availability. Available slots for General are Monday at 10:00 AM and Tuesday at 2:00 PM."
        
    return {
        "answer": answer,
        "sources": []
    }

def process_query(question: str):
    """
    Agentic Router:
    Decides whether to use the RAG pipeline or a specific tool based on user intent.
    """
    question_lower = question.lower()
    
    if "appointment" in question_lower or "book" in question_lower or "schedule" in question_lower:
        print("Agent routing to: Appointment Tool")
        return check_available_slots(question)
    else:
        print("Agent routing to: RAG Knowledge Base")
        return ask_question(question)