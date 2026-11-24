#!/usr/bin/env python3
"""One Letter for Your Day.

Writes exactly one letter to /output/entry.txt: the letter O.

O stands for "Overslept" -- the day summed up in a single picture:
eyes opening at noon, the alarm snoozed into silence, the whole
morning already gone before the day even started. It is vivid (you
can see the clock), funny (sleep won the day), and true (everyone
has lost a morning this way). The letter O even looks the part:
round, like a clock face and like a mouth mid-yawn.

Standard library only. Deterministic: the same single byte, every run.
"""

import os

LETTER = "O"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Exactly one character, no trailing newline: the gate wants
    # UTF-8 text of 1 to 1 characters, and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
