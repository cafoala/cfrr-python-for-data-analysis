# Python for Data Analysis

Two three-hour sessions for the [Coding for Reproducible Research (CfRR)](https://coding-for-reproducible-research.github.io/CfRR_Courses/) programme at the University of Exeter. The course teaches NumPy, pandas, matplotlib and Plotly, with a little SciPy for statistics, through one question: **was summer 2026 actually unusual, or does it just feel that way?** Learners answer it with Met Office monthly weather records for Oxford (from 1853) and Lerwick (from 1930).

- **Day 1, getting to know the data:** warm up on the Python you'll need, load a messy text file, find out why it misbehaves, clean it without throwing information away, give every month a date, pick out rows by label, position and boolean mask, decide what to do about missing data, and summarise with `groupby`.
- **Day 2, answering the question:** plot it with `fig, ax` and Plotly, see the NumPy arrays underneath pandas, fit a trend and test how sure it is, bring in a second station with a `load_station()` function moved into a file of its own, combine and resample the two records, and check the analysis reproduces.

Prerequisite: the CfRR [Introduction to Python](https://coding-for-reproducible-research.github.io/CfRR_Courses/individual_modules/section_landing_pages/introduction_to_python.html) course, or equivalent.

## Setup

You don't need git or a copy of this repository. Before the first session, follow the [CfRR setup](https://coding-for-reproducible-research.github.io/CfRR_Courses/programme_information/python_for_data_analysis.html): a course folder, a `.venv` inside it, and the libraries installed. Then add Plotly, which that install command leaves out, and SciPy, which Day 2 uses for statistics:

```bash
pip install plotly scipy
```

Before the first session you will be sent `python-for-data-analysis.zip`: both days' notebooks, their solutions and the data. Extract it into your course folder. On Windows, right-click it and choose **Extract All**: double-clicking only looks inside the zip, and the notebooks won't find their data. You don't need an internet connection in the session.

## During the course

The sessions are a code-along. Start `jupyter lab` in your course folder, open the extracted `python-for-data-analysis` folder, and open that day's notebook, `day1.ipynb` or `day2.ipynb`. The explanations are written for you and most code cells are empty: type the code into them as the instructor does. If you fall behind, copy the cell you missed from that day's solutions notebook, next to it in the same folder, which has every cell filled in. You can also read the solutions here:

- [Day 1 solutions](notebooks/day1_solutions.ipynb)
- [Day 2 solutions](notebooks/day2_solutions.ipynb)

## What's here

| Path | What it is |
|---|---|
| `notebooks/` | Exactly what goes in the learners' zip, and nothing else |
| `notebooks/day1.ipynb`, `notebooks/day2.ipynb` | What learners fill in: the explanations, with empty code cells |
| `notebooks/day1_solutions.ipynb` | Day 1 complete: every cell and its output |
| `notebooks/day2_solutions.ipynb` | Day 2 complete |
| `notebooks/data/` | Pinned snapshots of the Met Office files; see `notebooks/data/README.md` |
| `instructor/` | Demo notebooks: the solutions plus the instructor's speaker notes. `data` here is a link to `notebooks/data` |
| `instructor_notes.md` | How to run the code-along, and the timetable for both days |
| `tools/make_notebooks.py` | Builds the learners' notebooks and the solutions notebooks from the demo notebooks |
| `tests/test_notebooks.py` | Runs every demo notebook and checks the learners' notebooks are up to date |

## Maintaining the course

The **demo notebooks in `instructor/` are the source**. Edit those, never the notebooks in `notebooks/`. Three cell tags matter:

| Tag | Meaning |
|---|---|
| `instructor` | A speaker note. Left out of the learners' notebooks |
| `given` | A code cell learners get already filled in: setup, or syntax not worth typing. Every other code cell is empty in `dayN.ipynb` |
| `raises-exception` | Shows learners a real error on purpose. The tests allow it to fail |

Tags are cell metadata, not buttons. VS Code shows them as chips above each cell, and the `x` on a chip deletes the tag. In JupyterLab they sit under the property inspector (the gear icon in the right sidebar). The learners' notebooks carry no tags.

After editing, rerun the demo notebook from the top (so its outputs are current), rebuild the learners' notebooks and run the checks:

```bash
uv run python tools/make_notebooks.py
uv run python tests/test_notebooks.py
```

They run each demo notebook from a fresh kernel, and fail if a learners' notebook is out of date.

To work on the course itself, clone the repository and run `uv sync`, or use `pip install -r requirements.txt` in a virtual environment.

### Building the learners' zip

Everything in `notebooks/` goes to learners. Commit, then build the zip from that commit:

```bash
mkdir -p dist
git archive --format=zip --prefix=python-for-data-analysis/ -o dist/python-for-data-analysis.zip HEAD:notebooks
```

`git archive` takes only committed files, so the zip never picks up saved figures and CSV files, the `helper.py` that Day 2 writes, `.ipynb_checkpoints` or uncommitted edits, and the data files keep their exact bytes. If you change anything after sending the zip, rebuild it and send it again.

To change the data, replace the files in `notebooks/data/`, update the date and checksums in its README, rerun the demo notebooks and update the numbers in the speaker notes.

`instructor/data` is a symbolic link, so the demo notebooks run in place. On Windows, git checks them out as links only with `core.symlinks` enabled.

To change dependencies, use `uv add <package>` (or edit `pyproject.toml` and run `uv lock`), then regenerate the pip file:

```bash
uv export --format requirements.txt --no-hashes --no-dev --no-emit-project -o requirements.txt
```

Test on the oldest supported Python as well as the newest. pandas 3 needs Python 3.11 or later, so Python 3.10 learners get pandas 2.3, which shows text columns as `object` rather than `str` and words some error messages differently.

## Licence and attribution

Course material: see [LICENSE](LICENSE).

Weather data: Met Office historic station data. Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
