"""Build each learners' solutions notebook from its instructor demo notebook.

The demo notebooks in instructor/ are the source. Markdown cells tagged
"instructor" (speaker notes) are left out, and every other tag is removed,
so learners get a plain notebook with every cell and its output.

Run from the repository root after editing a demo notebook:

    python tools/make_solutions.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAIRS = {
    ROOT / "instructor" / "day1_demo.ipynb": ROOT / "notebooks" / "day1_solutions.ipynb",
    ROOT / "instructor" / "day2_demo.ipynb": ROOT / "notebooks" / "day2_solutions.ipynb",
}


def build(demo):
    nb = json.loads(demo.read_text(encoding="utf-8"))
    nb["cells"] = [cell for cell in nb["cells"]
                   if "instructor" not in cell.get("metadata", {}).get("tags", [])]
    for cell in nb["cells"]:
        cell.get("metadata", {}).pop("tags", None)
    return json.dumps(nb, indent=1, ensure_ascii=False) + "\n"


if __name__ == "__main__":
    for demo, solutions in PAIRS.items():
        solutions.write_text(build(demo), encoding="utf-8")
        print(f"{demo.relative_to(ROOT)} -> {solutions.relative_to(ROOT)}")
