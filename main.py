"""Dad Joke Showdown entry.

Writes exactly one dad joke (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, fully deterministic.
"""

import os

JOKE = "My son asked why I always carry a pencil. I said, 'In case I need to draw the line somewhere.'"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
