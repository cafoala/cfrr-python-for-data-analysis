"""Check the course notebooks.

- the demo notebooks and the Day 2 checkpoint run top to bottom from a fresh kernel
- each solutions notebook is up to date with its demo notebook

The notebooks download their data, so this needs an internet connection.

Run from the repository root:

    python tests/test_notebooks.py
"""

import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from make_solutions import PAIRS, build  # noqa: E402

RUN_IN_FULL = [*PAIRS, ROOT / "notebooks" / "day2_checkpoint.ipynb"]


def test_notebooks_run_top_to_bottom():
    # Cells tagged "raises-exception" are allowed to fail; any other error fails the test
    for path in RUN_IN_FULL:
        nb = nbformat.read(path, as_version=4)
        NotebookClient(nb, timeout=600, kernel_name="python3",
                       resources={"metadata": {"path": str(path.parent)}}).execute()


def test_solutions_up_to_date():
    for demo, solutions in PAIRS.items():
        assert solutions.read_text(encoding="utf-8") == build(demo), \
            f"{solutions.name} is stale: run python tools/make_solutions.py"


if __name__ == "__main__":
    for test in [test_solutions_up_to_date, test_notebooks_run_top_to_bottom]:
        test()
        print("ok", test.__name__)
