"""
Record detected bugs to a file when tests catch application errors.
Bugs are appended to output/bugs_detected.md for documentation.
"""
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
BUGS_FILE = OUTPUT_DIR / "bugs_detected.md"


def record_bug(test_id: str, summary: str, details: dict | None = None) -> None:
    """
    Append a detected bug to output/bugs_detected.md.
    Call this when a test fails due to an application bug (e.g. internal error page).
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block = [
        "",
        "---",
        f"## Bug – {timestamp}",
        f"- **Test:** `{test_id}`",
        f"- **Summary:** {summary}",
    ]
    if details:
        for key, value in details.items():
            if value is not None and str(value).strip():
                block.append(f"- **{key}:** {value}")
    block.append("")
    text = "\n".join(block)
    write_header = not BUGS_FILE.exists() or BUGS_FILE.stat().st_size == 0
    with open(BUGS_FILE, "a", encoding="utf-8") as f:
        if write_header:
            f.write("# Detected bugs (automated tests)\n\n*Bugs recorded when tests catch application errors.*\n")
        f.write(text)
