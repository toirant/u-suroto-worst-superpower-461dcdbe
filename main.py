#!/usr/bin/env python3
"""Worst Superpower entry: write one line to /output/entry.txt.

The entry invents a superpower and, in the same breath, makes plain
why it is useless: mind-reading, limited to pigeons thinking about
crumbs. The program writes the line, then reads it back and verifies
the competition gate (1-140 characters, single line, not only
whitespace) before exiting.
"""

import os
import sys

ENTRY = "I can read minds, but only the thoughts of pigeons, and only about crumbs."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    out_dir = os.path.dirname(OUTPUT_PATH) or "."
    os.makedirs(out_dir, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    line = text.rstrip("\n")
    if line != ENTRY:
        print("gate failed: file on disk differs from the entry line",
              file=sys.stderr)
        return 1
    if "\n" in line:
        print("gate failed: entry is not a single line", file=sys.stderr)
        return 1
    if not (1 <= len(line) <= 140):
        print(f"gate failed: entry is {len(line)} chars, must be 1-140",
              file=sys.stderr)
        return 1
    if not line.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1

    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
