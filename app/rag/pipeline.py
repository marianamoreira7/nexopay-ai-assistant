import logging

from app.rag.loader import load_faq
from app.services.llm import ask_llm, build_system_prompt


def answer(question: str) -> str:
    faq=load_faq()
    return f"[teste] Voce perguntou: {question} faq carregado {len(faq)} caractteres"


FALLBACK = (
    "Desculpe, tive um problema para responder agora. "
    "Tente novamente em instantes."
)

logger = logging.getLogger(__name__)

def answer_v2(question: str) -> str:
    system = build_system_prompt(load_faq())

    try:
        return ask_llm(system, question)

    except Exception:
        logger.exception("Falha ao chamar a LLM")
        return FALLBACK
    