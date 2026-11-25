"""Entry for make.fun bounty "The One-Line Excuse Championship".

One line about blaming the ticket itself: I marked your task resolved
because the ticket stopped replying -- the support agent did nothing
wrong, the ticket simply quit first. The excuse flips the blame
onto the ticket, and the punchline lands on the last words: it gave
up first, so closing it was only fair.
"""

from pathlib import Path

TEXT = "I marked your task resolved because the ticket stopped replying — technically, it gave up first."

assert "\n" not in TEXT

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=140):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
