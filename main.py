#!/usr/bin/env python3
"""One-line roast of an everyday gadget.

Writes a single original roast line to /output/entry.txt.
Standard library only, no network, no randomness:
two runs produce byte-identical output.
"""

import os

ROAST = "My phone's battery dies at 4 p.m. daily — the only thing in my life with a real work-life balance."
# The joke: the phone quits on time every day, so it ironically has better
# boundaries than its owner, who never does.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert "\n" not in ROAST and "\r" not in ROAST, "roast must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
