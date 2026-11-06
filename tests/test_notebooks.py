"""Check the course notebooks.

- the demo notebooks and the Day 2 checkpoint run top to bottom from a fresh kernel
- the learners' notebooks are up to date with the demo notebooks
- in the notebooks learners fill in, only cells tagged "given" keep their code

Run from the repository root:

    python tests/test_notebooks.py
"""

import json
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from make_notebooks import DEMOS, build, targets  # noqa: E402

RUN_IN_FULL = [*DEMOS, ROOT / "notebooks" / "day2_checkpoint.ipynb"]


def test_notebooks_run_top_to_bottom():
    # Cells tagged "raises-exception" are allowed to fail; any other error fails the test
    for path in RUN_IN_FULL:
        nb = nbformat.read(path, as_version=4)
        NotebookClient(nb, timeout=600, kernel_name="python3",
                       resources={"metadata": {"path": str(path.parent)}}).execute()


def test_learner_notebooks_up_to_date():
    for demo in DEMOS:
        for path, contents in targets(demo).items():
            assert path.read_text(encoding="utf-8") == contents, \
                f"{path.name} is stale: run python tools/make_notebooks.py"


def test_only_given_cells_keep_code():
    for demo in DEMOS:
        cells = json.loads(demo.read_text(encoding="utf-8"))["cells"]
        given = sum("given" in cell["metadata"].get("tags", []) for cell in cells)
        code = [cell for cell in json.loads(build(demo, blanks=True))["cells"]
                if cell["cell_type"] == "code"]
        assert sum(bool(cell["source"]) for cell in code) == given > 0, demo.name
        assert not any(cell["outputs"] for cell in code), demo.name


if __name__ == "__main__":
    for test in [test_only_given_cells_keep_code, test_learner_notebooks_up_to_date,
                 test_notebooks_run_top_to_bottom]:
        test()
        print("ok", test.__name__)
