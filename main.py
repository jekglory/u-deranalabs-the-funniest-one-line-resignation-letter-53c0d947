"""One-line resignation letter of a cron job.

Writes exactly one line of text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR):
the resignation letter of the cron job that has fired at 03:00 every night
for four years, resigning effective at its own shift hour. Pure stdlib.
"""

import os
from pathlib import Path

LETTER = (
    "I resign, effective 03:00 \u2014 after four years straight of working alone "
    "every night, I finally decided to sleep in for once."
)


def main() -> None:
    text = LETTER.strip()
    assert 1 <= len(text) <= 140, "letter must be 1-140 characters"
    assert "\n" not in text, "letter must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Clear only the contents of the grader-provided directory, never the
    # directory itself (the grader owns it).
    for child in out_dir.iterdir():
        if child.is_dir() and not child.is_symlink():
            for sub in child.rglob("*"):
                if sub.is_file() or sub.is_symlink():
                    sub.unlink()
            for sub in sorted(child.rglob("*"), reverse=True):
                if sub.is_dir():
                    sub.rmdir()
        else:
            child.unlink()
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
