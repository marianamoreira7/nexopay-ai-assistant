from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_whatsapp_webhook(monkeypatch):
    monkeypatch.setattr("app.main.answer", lambda q: f"resposta para: {q}")

    response = client.post(
        "/webhook/whatsapp",
        data={"Body": "oi", "From": "whatsapp:+5551999999999"},
    )

    assert response.status_code == 200
    assert "resposta para: oi" in response.text
