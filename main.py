"""Office Artifacts: The One-Line Placard Contest.

Writes the champion placard line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The entry is a museum placard for a fire
extinguisher, treated as an ancient artifact: a guardian god, inspected
yearly, invoked never.
"""

import os

ENTRY = "Fire extinguisher, c. 1994. Red steel, untouched. A guardian god, inspected yearly, invoked never. Donated by Health & Safety."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
