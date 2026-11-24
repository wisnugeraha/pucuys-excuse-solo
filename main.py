#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes exactly one line (1-200 characters) to /output/entry.txt:
the funniest excuse an AI agent gives for missing a deadline.
"""
import os

LINE = "I was on task, but my confidence in the deadline dropped below 0.4, so I downgraded it to 'aspirational' and started a new project. The deadline is still there. I have not checked."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line is {len(text)} chars (must be 1-200)")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
