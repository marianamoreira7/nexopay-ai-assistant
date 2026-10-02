import logging

from app.rag.loader import load_faq
from app.services.llm import ask_llm, build_system_prompt

FALLBACK = (
    "Desculpe, tive um problema para responder agora. Tente novamente em instantes."
)

logger = logging.getLogger(__name__)


def answer(question: str) -> str:
    system = build_system_prompt(load_faq())

    try:
        return ask_llm(system, question)

    except Exception:
        logger.exception("Falha ao chamar a LLM")
        return FALLBACK
