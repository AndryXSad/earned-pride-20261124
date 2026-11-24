"""One Line of Earned Pride -- entry program.

Design: the entry is a single fixed line of text, written for the judge's
brief -- a quiet, earned moment of pride for a real person in a concrete
scene. Six years of mending other people's wedding dresses, then the last
stitch on her own: the effort is felt inside the line, the pride arrives
with the final words, and nothing is asserted, congratulated or explained.

The program writes that one line, and only that line, to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable is
unset), and refuses to write anything that falls outside the 1-240
character gate.
"""

import os
import sys

ENTRY = (
    "For six years she mended other people's wedding dresses; "
    "today she sewed the last stitch on her own."
)

MIN_CHARS = 1
MAX_CHARS = 240


def output_dir():
    """Where the grader expects the entry; never the repository itself."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    text = ENTRY
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        print(f"entry is {len(text)} characters, outside 1-240", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be one line with no surrounding whitespace", file=sys.stderr)
        return 1
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(out_path, encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            print("written entry does not match", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
