"""Save/load last successfully registered user for login tests."""
import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
CREDENTIALS_FILE = OUTPUT_DIR / "last_registered_user.json"


def save_registered_user(email: str, password: str) -> None:
    """Save email and password after successful registration so login tests can use them."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
        json.dump({"email": email, "password": password}, f, indent=2)


def load_registered_user() -> dict:
    """Load last registered user. Returns dict with 'email' and 'password'. Raises if file missing."""
    with open(CREDENTIALS_FILE, encoding="utf-8") as f:
        return json.load(f)
