# Python for Data Analysis

Two three-hour sessions for the [Coding for Reproducible Research (CfRR)](https://coding-for-reproducible-research.github.io/CfRR_Courses/) programme at the University of Exeter. The course teaches NumPy, pandas, matplotlib, Plotly and scikit-learn through one question: **was summer 2026 actually unusual, or does it just feel that way?** Learners answer it with Met Office monthly weather records for Oxford (from 1853) and Lerwick (from 1930).

- **Day 1, getting to know the data:** load a messy text file, find out why it misbehaves, clean it without throwing information away, see the NumPy arrays underneath, decide what to do about missing data, and summarise with `groupby`.
- **Day 2, answering the question:** plot it with `fig, ax` and Plotly, fit a trend, bring in a second station with a tested `load_station()` function, try some machine learning, and check the analysis reproduces.

Prerequisite: the CfRR [Introduction to Python](https://coding-for-reproducible-research.github.io/CfRR_Courses/individual_modules/section_landing_pages/introduction_to_python.html) course, or equivalent.

## Setup

You don't need git or a copy of this repository. Before the first session, follow the [CfRR setup](https://coding-for-reproducible-research.github.io/CfRR_Courses/programme_information/python_for_data_analysis.html): a course folder, a `.venv` inside it, and the libraries installed. Then add Plotly, which that install command leaves out:

```bash
pip install plotly
```

You will need an internet connection in the session: the notebooks download the data themselves.

## During the course

The sessions are a code-along. Each day, start `jupyter lab` in your course folder, create a new notebook (File > New > Notebook) and type the code as the instructor does. If you fall behind, copy the cell you missed from that day's solutions notebook, which you can read here on GitHub:

- [Day 1 solutions](notebooks/day1_solutions.ipynb)
- [Day 2 solutions](notebooks/day2_solutions.ipynb)

## What's here

| Path | What it is |
|---|---|
| `notebooks/day1_solutions.ipynb` | Day 1 complete: every cell, its output, and the answer to every exercise |
| `notebooks/day2_checkpoint.ipynb` | Day 1's cleaning in one place; Day 2 downloads it and runs it with `%run` |
| `notebooks/day2_solutions.ipynb` | Day 2 complete |
| `instructor/` | Demo notebooks: the solutions plus the instructor's speaker notes |
| `instructor_notes.md` | How to run the code-along, and the timetable for both days |
| `data/` | Pinned snapshots of the Met Office files, which the notebooks download; see `data/README.md` |
| `tools/make_solutions.py` | Builds each solutions notebook from its demo notebook |
| `tests/test_notebooks.py` | Runs every notebook and checks the solutions notebooks are up to date |

## Maintaining the course

The **demo notebooks in `instructor/` are the source**. Edit those, never the solutions notebooks. Speaker notes are markdown cells tagged `instructor`; the build leaves them out of the solutions notebooks. Cells tagged `raises-exception` show learners a real error on purpose, and the tests allow them to fail.

Tags are cell metadata, not buttons. VS Code shows them as chips above each cell, and the `x` on a chip deletes the tag. In JupyterLab they sit under the property inspector (the gear icon in the right sidebar). The solutions notebooks carry no tags.

After editing, rerun the demo notebook from the top (so its outputs are current), rebuild the solutions notebooks and run the checks:

```bash
uv run python tools/make_solutions.py
uv run python tests/test_notebooks.py
```

The tests need an internet connection. They run each demo notebook and the checkpoint from a fresh kernel, and fail if a solutions notebook is out of date.

To work on the course itself, clone the repository and run `uv sync`, or use `pip install -r requirements.txt` in a virtual environment.

### Changing the data or the checkpoint

The notebooks download from the tag `snapshot-2026-10-29`, not from `main`, so changing those files here changes nothing for learners. To release a change:

1. Pick a new tag name and change `BASE` in the checkpoint to it. The tagged checkpoint has to name its own tag.
2. Commit the data and the checkpoint, tag that commit, and push both.
3. Change `BASE` in the demo notebooks to the new tag, rerun them, rebuild the solutions and run the tests.

To change dependencies, use `uv add <package>` (or edit `pyproject.toml` and run `uv lock`), then regenerate the pip file:

```bash
uv export --format requirements.txt --no-hashes --no-dev --no-emit-project -o requirements.txt
```

Test on the oldest supported Python as well as the newest. pandas 3 needs Python 3.11 or later, so Python 3.10 learners get pandas 2.3, which shows text columns as `object` rather than `str` and words some error messages differently.

## Licence and attribution

Course material: see [LICENSE](LICENSE).

Weather data: Met Office historic station data. Contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
