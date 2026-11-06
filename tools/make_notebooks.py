"""Build the learners' notebooks from the instructor demo notebooks.

The demo notebooks in instructor/ are the source. From each one this builds:

- notebooks/dayN.ipynb, which learners fill in during the session: every code
  cell is emptied and its output cleared, except cells tagged "given", which
  keep their code
- notebooks/dayN_solutions.ipynb: every cell, with its output

Both leave out the markdown cells tagged "instructor" (speaker notes) and
carry no tags.

Run from the repository root after editing a demo notebook:

    python tools/make_notebooks.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEMOS = [ROOT / "instructor" / "day1_demo.ipynb", ROOT / "instructor" / "day2_demo.ipynb"]


def build(demo, blanks=False):
    nb = json.loads(demo.read_text(encoding="utf-8"))
    nb["cells"] = [cell for cell in nb["cells"]
                   if "instructor" not in cell["metadata"].get("tags", [])]
    for cell in nb["cells"]:
        tags = cell["metadata"].pop("tags", [])
        if blanks and cell["cell_type"] == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
            if "given" not in tags:
                cell["source"] = []
    return json.dumps(nb, indent=1, ensure_ascii=False) + "\n"


def targets(demo):
    """The learners' notebooks built from one demo notebook: {path: contents}."""
    day = demo.stem.removesuffix("_demo")
    return {
        ROOT / "notebooks" / f"{day}.ipynb": build(demo, blanks=True),
        ROOT / "notebooks" / f"{day}_solutions.ipynb": build(demo),
    }


if __name__ == "__main__":
    for demo in DEMOS:
        for path, contents in targets(demo).items():
            path.write_text(contents, encoding="utf-8")
            print(f"{demo.relative_to(ROOT)} -> {path.relative_to(ROOT)}")
