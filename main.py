"""One Star, Five Stars for the Food — make.fun entry.

Writes a single sentence (an alien tourist's one-star review of Earth
that still compliments the food) to /output/entry.txt.

The entry length is validated at runtime against the contest's
1–200 character gate before anything is written.

Python 3.13 standard library only.
"""

import os

# Contest gate: entry must be between 1 and 200 characters inclusive.
MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 200

LINE = (
    "One star: your species photographs its food instead of eating it, "
    "queues for everything, and charges for water \u2014 but the satay "
    "alone is worth the eleven-light-year trip."
)


def main() -> None:
    if not MIN_ENTRY_CHARS <= len(LINE) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} characters, "
            f"got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
