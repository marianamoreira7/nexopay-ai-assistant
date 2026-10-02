
import logging
import os

from google import genai
from anthropic import Anthropic
from dotenv import load_dotenv

from app.rag.loader import load_faq

load_dotenv()
logger = logging.getLogger(__name__)

MODEL = os.getenv("LLM_MODEL", "claude-haiku-4-5-20251001")

FALLBACK = (
    "Desculpe, tive um problema para responder agora. "
    "Tente novamente em instantes."
)


def build_system_prompt(faq: str) -> str:
    return f"""Você é o assistente de atendimento da NexoPay,
uma fintech de pagamentos para pequenos negócios.

Responda às perguntas dos lojistas usando APENAS as
informações do FAQ abaixo.

Regras:
- Se a resposta não estiver no FAQ, diga que não tem essa
  informação e sugira falar com o suporte pelo aplicativo.
- Nunca invente valores de tarifas, taxas ou prazos.
- Responda em português, de forma curta e direta.
- Utilize linguagem natural, adequada para WhatsApp.
- Nunca peça senha, token ou código de autenticação.

<faq>
{faq}
</faq>"""


def ask_llm(system: str, question: str) -> str:
    client = Anthropic()
    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        system=system,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text
