"""A tiny one-line review generator.

Running this script produces the short review text for the bounty and
stores it in a file, so the entry can be checked and submitted as-is.
"""

from pathlib import Path


# The wording below is the whole submission, kept as one plain string.
REVIEW_TEXT = "1 star. Only works nights, vanishes for a week every month, and still floods my beach twice a day. Would not recommend."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    review = REVIEW_TEXT.strip()

    if not review:
        raise SystemExit("Error: the review text is empty.")

    if "\n" in review or "\r" in review:
        raise SystemExit("Error: the review must fit on a single line.")

    if not 1 <= len(review) <= 120:
        raise SystemExit(
            f"Error: the review has {len(review)} characters, "
            "but it must be between 1 and 120 characters long."
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(review, encoding="utf-8")

    print(len(review))


if __name__ == "__main__":
    main()
