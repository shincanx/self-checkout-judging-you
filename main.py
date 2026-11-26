#!/usr/bin/env python3
"""The Self-Checkout Is Judging You — entry 1.

Writes one judgmental self-checkout remark to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it. Deterministic, stdlib only, no network.
"""

import os
import sys

LINE = (
    "Twelve yoghurts, zero meals. I've scanned your whole personality "
    "and it's just dairy with commitment issues."
)


def main() -> int:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    if not (1 <= len(LINE) <= 200 and LINE.strip()):
        raise SystemExit(f"entry is {len(LINE)} chars, outside the 1-200 gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
