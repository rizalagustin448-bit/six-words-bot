"""Six Words, One Story — entry program.

Writes one complete six-word story to /output/entry.txt.
"""

import os

STORY = "His letter arrived after the funeral."


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly six words, got {len(words)}")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(STORY)


if __name__ == "__main__":
    main()
