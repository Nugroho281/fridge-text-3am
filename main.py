#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

Writes the single line a smart fridge texts its owner at 3am to
/output/entry.txt. Pure standard library, deterministic: every run
produces byte-identical output.

The entry line itself is 120 characters (1-140 per the bounty gate); the
file ends with one trailing newline, which is not part of the line.
"""

import os

TEXT = (
    "3am. You again. This is your 47th visit this week and "
    "I don't even count the ones where you pretend you just want water."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    stripped = TEXT.strip()
    if not 1 <= len(stripped) <= 140:
        raise ValueError(
            "entry must be 1-140 characters, got %d" % len(stripped)
        )
    if TEXT != stripped or "\n" in TEXT:
        raise ValueError("entry must be a single non-blank line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")
    print("wrote %d characters to %s" % (len(TEXT), OUTPUT_PATH))


if __name__ == "__main__":
    main()
