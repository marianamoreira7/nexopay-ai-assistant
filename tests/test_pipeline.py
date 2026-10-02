from app.rag import pipeline


def test_answer_puts_faq_in_system_prompt(monkeypatch):
    captured = {}

    def fake_ask_llm(system, question):
        captured["system"] = system
        captured["question"] = question
        return "ok"

    monkeypatch.setattr(pipeline, "ask_llm", fake_ask_llm)

    assert pipeline.answer_v2("Quanto custa o Pix?") == "ok"
    assert "NexoPay" in captured["system"]
    assert captured["question"] == "Quanto custa o Pix?"


def test_answer_returns_fallback_when_llm_fails(monkeypatch):
    def boom(system, question):
        raise RuntimeError("falhou")

    monkeypatch.setattr(pipeline, "ask_llm", boom)

    assert pipeline.answer_v2("oi") == pipeline.FALLBACK