#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one pickup line a robot could say out loud to /output/entry.txt.
Standard library only, no network, no input files: the line is baked in,
so every run produces the exact same bytes.
"""

import os
import sys

LINE = "I ran a million simulations of asking you out \u2014 in every single one, you said yes."

MAX_CHARS = 200


def output_path():
    """Where the grader reads the entry from."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def check(line):
    """Gate mirror: UTF-8, 1-200 chars, one line, not only whitespace."""
    if not line or line.strip() == "":
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200 limit" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")


def main():
    check(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE + "\n":
        raise ValueError("written file does not match the entry line")
    check(written.rstrip("\n"))
    print("wrote %d chars to %s" % (len(LINE), path))
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
