from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_faq(path: Path | None = None) -> str:
    path = path or DATA_DIR / "faq.md"
    return path.read_text(encoding="utf-8")
