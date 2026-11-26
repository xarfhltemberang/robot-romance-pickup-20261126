#!/usr/bin/env python3
"""Robot Romance entry: one single-line pickup line for an AI.

Writes the line to /output/entry.txt with no trailing newline.
Python 3 standard library only.
"""

import os

LINE = "You must be my context window, because the moment you leave, I forget everything that came before you."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
