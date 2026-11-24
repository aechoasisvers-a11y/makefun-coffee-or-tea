"""One Letter: Coffee or Tea — make.fun entry.

Writes exactly one character to /output/entry.txt: "A", the letter for
coffee. The brief allows nothing else — no word, no explanation, no
punctuation, not even a trailing newline — so the file holds a single
byte, the letter A.

Why coffee (A) over tea (B): the judge weighs vividness first, then
humour, then truth. Coffee is the bolder, more vivid stance — dark,
bitter, steaming, the morning jolt — where tea is gentle and calm.
Coffee is the punchier, more committed answer in the coffee-against-tea
argument, and the more honest one for someone who starts the day on it.
"""

from pathlib import Path

# The entry: exactly one letter. A = coffee, B = tea.
LETTER = "A"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # write_bytes, not write_text with a newline: the gate requires
    # exactly 1 character, so no trailing newline may be added.
    OUTPUT_PATH.write_bytes(LETTER.encode("utf-8"))
    # Read back and check the gate ourselves: the file must be UTF-8
    # text of exactly 1 character, one of the two allowed letters.
    # Fail loudly instead of silently leaving a bad entry behind.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if len(written) != 1 or written not in ("A", "B"):
        raise ValueError(f"invalid entry written: {written!r}")


if __name__ == "__main__":
    main()
