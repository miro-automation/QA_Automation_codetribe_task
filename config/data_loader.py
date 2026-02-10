"""Load static data from JSON. Used by tests and pages."""
from pathlib import Path
import json


_STATIC_DATA_PATH = Path(__file__).resolve().parent / "static_data.json"
_cached: dict | None = None


def get_static_data() -> dict:
    """Load and cache static_data.json. Returns dict (e.g. Products.Build)."""
    global _cached
    if _cached is None:
        with open(_STATIC_DATA_PATH, encoding="utf-8") as f:
            _cached = json.load(f)
    return _cached


def get_value(section: str, key: str) -> str:
    """Get one value, e.g. get_value('Products', 'Build') -> 'Build'."""
    data = get_static_data()
    return data[section][key]
