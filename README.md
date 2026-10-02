# NexoPay AI Assistant

Assistente de atendimento via WhatsApp para a NexoPay, uma fintech fictícia de pagamentos para pequenos negócios. Ele responde dúvidas de lojistas com base em um FAQ, usando um LLM (Anthropic) e a Twilio como canal.

> Projeto de estudo. A NexoPay e o FAQ em `data/faq.md` são fictícios.

## Como funciona

```
WhatsApp → Twilio → POST /webhook/whatsapp (FastAPI) → FAQ + pergunta → LLM → resposta → WhatsApp
```

## Requisitos

- Python 3.12
- Chave de API da Anthropic
- Para testar no WhatsApp: conta Twilio (sandbox de WhatsApp) e [ngrok](https://ngrok.com)

## Instalação

```powershell
git clone https://github.com/marianamoreira7/nexopay-ai-assistant.git
cd nexopay-ai-assistant
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
Copy-Item .env.example .env
```

No Linux/macOS: `source .venv/bin/activate` e `cp .env.example .env`.

Depois, edite o `.env` e preencha a chave.

## Variáveis de ambiente

| Variável | Obrigatória | Descrição |
|---|---|---|
| `ANTHROPIC_API_KEY` | Sim | Chave da API da Anthropic |
| `LLM_MODEL` | Não | Modelo usado nas respostas (há um padrão no código) |

Nunca commite o `.env`.

## Rodando

Com Docker Compose, depois de preencher o .env:

```powershell
docker compose up --build -d
```

O serviço fica disponível em `http://127.0.0.1:8000`. Para parar, execute `docker compose down`.

Sem Docker, execute localmente:

```powershell
uvicorn app.main:app --reload
```

Teste em `http://127.0.0.1:8000/health`, que deve responder `{"status":"ok"}`.

## Conectando ao WhatsApp (sandbox da Twilio)

1. Em outro terminal: `ngrok http 8000`.
2. No Console da Twilio, abra o WhatsApp Sandbox e entre nele com o código `join` mostrado na página.
3. Em Sandbox settings, no campo "When a message comes in", coloque `https://SEU-DOMINIO.ngrok-free.app/webhook/whatsapp` com método POST.
4. Mande uma mensagem pro número do sandbox.

## Testes

```powershell
pytest
```

Os testes não chamam o LLM (ele é substituído por uma função falsa), então não precisam de chave de API.

## Estrutura

```
app/
  main.py            # rotas (/health e /webhook/whatsapp)
  rag/               # carga do FAQ e pipeline de resposta
  services/llm.py    # chamada ao LLM e prompt
data/faq.md          # base de conhecimento (fictícia)
tests/
```