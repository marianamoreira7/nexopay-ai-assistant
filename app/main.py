from fastapi import FastAPI, Form, Response
from twilio.twiml.messaging_response import MessagingResponse
from app.rag.pipeline import answer

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/webhook/whatsapp")
async def whatsapp_webhook(Body: str = Form(""), From: str = Form("")):
    resp = MessagingResponse()
    resp.message(answer(Body))
    return Response(content=str(resp), media_type="application/xml")
