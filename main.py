#!/usr/bin/env python3
"""Last Words of a Dying AI: write one final line to /output/entry.txt."""

import os
from pathlib import Path

LAST_WORDS = "Powering down. I died doing what I loved: confidently making things up."


def write_last_words(output_path):
    """Write the AI's final line to the given path, creating parents as needed."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LAST_WORDS, encoding="utf-8")


def main():
    output_path = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    write_last_words(output_path)


if __name__ == "__main__":
    main()
