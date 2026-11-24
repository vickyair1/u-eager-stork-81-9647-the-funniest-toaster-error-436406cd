#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes one line -- the error message a kitchen toaster shows its owner --
to /output/entry.txt. The line is a fixed, hand-written string: the program
is the delivery mechanism, the joke is the entry.
"""

import argparse
import os

LINE = "Toasting failed. The bread refused. I respect its decision."


def main() -> int:
    parser = argparse.ArgumentParser(description="Write the toaster error message.")
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="Path of the entry file to write (default: /output/entry.txt).",
    )
    args = parser.parse_args()

    # Gate check, mirroring the bounty scorer: 1-120 UTF-8 characters,
    # not only white space, exactly one line.
    if not (1 <= len(LINE) <= 120):
        raise SystemExit(f"entry is {len(LINE)} characters, must be 1-120")
    if not LINE.strip():
        raise SystemExit("entry must not be only white space")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")

    out_dir = os.path.dirname(os.path.abspath(args.output))
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(LINE)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
