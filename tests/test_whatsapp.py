from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_whatsapp_webhook():
    response = client.post("/webhook/whatsapp", data={"Body": "oi", "From":"whatsapp:+5553984034269"},
                           )
    assert response.status_code == 200
    assert "Recebi: oi" in response.text