from app.rag.loader import load_faq

def test_load_faq_not_empty():
    text = load_faq()
    assert len(text)>0