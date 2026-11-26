#!/usr/bin/env python3
"""One Line to Your Younger Self.

Writes a single line -- the one line the writer would send back to
his younger self -- to /output/entry.txt (and to ./entry.txt when run
locally). The line is fixed, specific and lived-in: a named boy, a
real age, a real object hidden for a real reason, and his father's
exact reply at 6 a.m.
"""

import os

LINE = (
    "Tommy, at twelve you hid Dad's wedding ring in the freezer so he "
    "couldn't pawn it \u2014 he found it at 6 a.m. and said, "
    "\"Nice try, son \u2014 now eat your toast.\""
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.count("\n") == 0
    assert LINE.endswith('."')  # one line, one sentence, no second sentence
    out_dir = "/output" if os.path.isdir("/output") else "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
