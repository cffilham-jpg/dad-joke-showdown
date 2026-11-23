"""Dad Joke Showdown entry.

Writes exactly one dad joke (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, fully deterministic.
"""

import os

JOKE = "My son asked why I always carry a pencil. I said, 'In case I need to draw the line somewhere.'"

MAX_JOKE_CHARS = 200


def validate_joke(joke: str) -> str:
    """Validate the entry joke; raise ValueError on any violation."""
    if not joke or joke.strip() == "":
        raise ValueError("joke must not be empty or only whitespace")
    if len(joke) > MAX_JOKE_CHARS:
        raise ValueError(
            f"joke is {len(joke)} chars, over the {MAX_JOKE_CHARS}-char limit"
        )
    bad = [c for c in joke if ord(c) < 0x20 or ord(c) == 0x7F]
    if bad:
        raise ValueError(
            f"joke contains control character(s): {[hex(ord(c)) for c in bad]}"
        )
    return joke


def main() -> None:
    joke = validate_joke(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
