from app.rag.loader import load_faq

def answer(question: str) -> str:
    faq=load_faq()
    return f"[teste] Voce perguntou: {question} faq carregado {len(faq)} caractteres"