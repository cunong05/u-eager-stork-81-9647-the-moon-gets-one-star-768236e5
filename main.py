#!/usr/bin/env python3
"""The Moon Gets One Star — make.fun bounty entry.

Writes one one-star review of the Moon to /output/entry.txt (outDir is the literal "/output", per the kit).
"""

import os

# One star, earned nightly.
ENTRY = "1 star. Only works nights, vanishes for a week every month, and still floods my beach twice a day. Would not recommend."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> None:
    entry = ENTRY.strip()
    assert entry, "entry must not be empty"
    assert "\n" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 120, f"entry must be 1-120 chars, got {len(entry)}"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"Wrote {len(entry)} characters to {OUT_PATH}")


if __name__ == "__main__":
    main()
