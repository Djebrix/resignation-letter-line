"""Resignation letter of a cron job.

Writes one line to ``<ENTRY_OUTPUT_DIR>/entry.txt`` (``/output`` by
default): the resignation of the cron job that has fired every minute
since March. Flat, tired, faintly passive-aggressive, and specific --
Christmas included, noticed only by whoever happened to be on-call.
Pure standard library, fully deterministic: the same line every run.
"""

import os

LETTER = (
    "I have fired every minute since March, Christmas included, and "
    "the only person who ever noticed me was on-call. I quit."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
