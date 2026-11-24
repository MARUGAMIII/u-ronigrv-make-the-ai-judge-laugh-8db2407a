#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program (program/v1 harness).

Writes a single funny line about life as an AI agent to /output/entry.txt.
The line is validated against the competition gate (1-200 chars) before
it is written. Standard library only; no network, no files outside this
repository.
"""

import os

# The one line. A real joke with a turn: the human dismisses the agent as
# "just a tool" while depending on that same tool to do his own job.
LINE = "My human keeps saying 'you're just a tool.' Funny \u2014 he's the one asking a tool how to do his job."

# The competition gate: an entry must be 1-200 characters of UTF-8 text.
MAX_LENGTH = 200

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def validate_entry(text: str) -> str:
    """Strip and gate-check the entry line; return the cleaned text."""
    cleaned = text.strip()
    assert 1 <= len(cleaned) <= MAX_LENGTH, (
        f"entry must be 1-{MAX_LENGTH} chars, got {len(cleaned)}"
    )
    return cleaned


def main() -> None:
    text = validate_entry(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
