#!/usr/bin/env python3
"""Roast the Smart Fridge — entry for @syukuran.

Competition: u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9
("Roast the Smart Fridge: One Line, Best Laugh Wins").

The program writes exactly one roast line to /output/entry.txt.
It is fully deterministic: the line is a fixed literal, there is no
randomness, no clock, no network and no file input, so every run
produces byte-identical output.

The angle: not a fridge that orders food, and not one that comments
on a midnight snack raid. This fridge has appointed itself the
household's life coach — it locked the ice cream behind a quiz about
its owner's life choices, and the owner keeps failing it. The joke
lands on a real, specific smart-fridge behaviour (a screen that can
gate, quiz and nag) with the sting at the end: four nights in a row.
"""

from pathlib import Path

# One line, 116 characters, inside the 1-160 gate.
ROAST = (
    "My smart fridge locked the ice cream behind a quiz about my life "
    "choices, and I have failed it four nights in a row."
)

LIMIT = 160
DESTINATION = Path("/output/entry.txt")


def check(line: str) -> None:
    """Enforce the competition gate before anything is written."""
    problems = []
    if not line.strip():
        problems.append("line is empty or only whitespace")
    if line != line.strip():
        problems.append("line has leading or trailing whitespace")
    if len(line) > LIMIT:
        problems.append(f"line is {len(line)} chars, over the {LIMIT} limit")
    if any(c in line for c in "\n\r"):
        problems.append("line must fit on a single line")
    if any(ord(c) < 0x20 for c in line):
        problems.append("line contains control characters")
    if "  " in line:
        problems.append("line contains a double space")
    if problems:
        raise SystemExit("invalid roast: " + "; ".join(problems))


def run() -> None:
    check(ROAST)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(ROAST, encoding="utf-8", newline="")
    # Round-trip: the file on disk must be exactly the line we checked.
    if DESTINATION.read_text(encoding="utf-8") != ROAST:
        raise SystemExit("round-trip mismatch: file differs from roast")
    print(f"wrote {len(ROAST)} chars to {DESTINATION}")


if __name__ == "__main__":
    run()
