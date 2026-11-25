"""One Star, Five Stars for the Food — make.fun entry.

Writes a single sentence (an alien tourist's one-star review of Earth
that still compliments the food) to /output/entry.txt.

Python 3.13 standard library only.
"""

import os

LINE = (
    "One star: your species photographs its food instead of eating it, "
    "queues for everything, and charges for water \u2014 but the satay "
    "alone is worth the eleven-light-year trip."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
