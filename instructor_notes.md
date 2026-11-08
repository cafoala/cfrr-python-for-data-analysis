# Instructor notes

The course is taught as a code-along. Everyone, you included, works in the same notebook, `notebooks/dayN.ipynb`. The explanations are written in it and most code cells are empty, and you fill them in on the projector while learners fill in their own copies.

Your script is the pair of **demo notebooks** in `instructor/`. Each one is the complete notebook plus speaker-note cells, set off as quotes, saying what to say, where to slow down, the misconceptions to watch for, and the numbers each cell should give. Notes marked **Optional** are questions to put to the room if the mood is right; the notebook reads fine without them. Numbers in the notes come from the data snapshot of 29 October 2026. If you change the snapshot, rerun the demo notebooks and update the notes.

Learners get two notebooks per day, both built from the demo notebook without the speaker notes:

- `dayN.ipynb`, which they fill in
- `dayN_solutions.ipynb`, with every cell filled in, next to it, which they copy from if they fall behind

Learners don't need git or a copy of this repository. Before the first session, send them `python-for-data-analysis.zip` (the README says how to build it): both days' notebooks, the solutions, the Day 2 checkpoint and the data. They extract it into the course folder from the CfRR setup, and nothing is downloaded in the session.

## Before each session

- Restart the kernel of the demo notebook. Hidden state catches instructors too.
- Project the learners' notebook, `dayN.ipynb`, from a freshly extracted copy of the zip, not the demo notebook, so your screen matches theirs. Keep the demo notebook on a second screen, a tablet or paper.
- Have the zip to hand, on a USB stick as well as by email, for anyone who arrives without it.
- Zoom JupyterLab to about 150% (Ctrl or Cmd and `+`) and use a light theme.
- Hand out two colours of sticky note: green for "done", red for "stuck, please come over".
- Learners on Python 3.10 have pandas 2.3; anyone on Python 3.11 or later who installed recently has pandas 3. Text columns show as `object` rather than `str`, and one error message is worded differently (Day 1, block 5).
- Day 2 uses `scipy.stats`. Nobody needs to install it: SciPy comes with scikit-learn, which the CfRR install command includes. If an import fails, `pip install scipy`.

## While live coding

- Type, don't paste. Typing sets a pace learners can follow, and your typos show them how to read errors.
- Say each line out loud as you type it, then run it.
- Run often: after every line or two when building a chart.
- Cells that are filled in already (setup, and a few cells of fiddly syntax) are for running and talking through, not typing.
- Walk round, or ask a helper to, and look for red sticky notes. When someone falls behind, point them to the solutions notebook rather than waiting for them.
- Slow down at the moments marked **Slow down** in the demo notebooks. They are the point of the block, not an obstacle to it.
- Copilot and chatbots will offer learners code. Say so openly. On both days the story stops to check a suggested fix (`errors="coerce"`) and finds it wrong.
- Day 1's practice block is the one time learners write code on their own. It ends the day, so if the morning overruns it is the block that shrinks. Stop typing, walk round, and only take answers on screen once most people have tried a few questions.

## Day 1: getting to know the data

Learners start in `day1.ipynb`, in the folder they extracted from the zip.

| Time | Block | Live-code |
|---|---|---|
| 10:00 (10 min) | 1. Welcome, the question and the data | Nothing. The question, then talk through "Meet the data" |
| 10:10 (10 min) | 2. Python warm-up | Whizz through: `str` methods on `"13.1*"`, `float`, `bool` and `and`, a list and a loop, a dict, a function |
| 10:20 (10 min) | 3. First look at the raw file | The setup cell; open the raw file and find what makes it awkward; the naive `read_csv` |
| 10:30 (15 min) | 4. Loading it properly | `sep` and read the error, then `skiprows` and `names` (with `status` for the `Provisional` rows), then `na_values`; anatomy of a DataFrame, `.columns` |
| 10:45 (20 min) | 5. The asterisk problem | `.info()`, find the `*` rows, `pd.to_numeric` fails loudly, the `errors="coerce"` trap, the loop, `.describe()` |
| 11:05 (10 min) | Break | |
| 11:15 (25 min) | 6. Picking rows: dates, labels and masks | About 10 minutes: `pd.to_datetime`, `.dt`, `format=`, `set_index`, `.loc` with dates, `.iloc`. About 15: one condition, `.loc[rows, columns]`, `&` and the missing-brackets trap, `~`, `.isin()` |
| 11:40 (20 min) | 7. NumPy | `.to_numpy()`, loop vs vectorised, NaN, the sunshine decision |
| 12:00 (15 min) | 8. Split-apply-combine | The plan in English, `groupby`, rank the Julys |
| 12:15 (5 min) | 9. Cliffhanger | The summer ranking; three reasons a ranking is not enough |
| 12:20 (10 min) | Break | |
| 12:30 (30 min) | 10. Practice | Learners work alone on 16 questions covering the whole day, as far as they get; in the last 5 to 10 minutes you go through two or three together, and they finish the rest in their own time |

## Day 2: answering the question

Learners start in `day2.ipynb`, in the same folder. Its first cell runs `day2_checkpoint.ipynb`, so nobody needs yesterday's notebook to work.

| Time | Block | Live-code |
|---|---|---|
| 10:00 (15 min) | 1. Recap and "Restart and run all" | `%run` the checkpoint; the hidden-state demo |
| 10:15 (45 min) | 2. Seeing it | `fig, ax` step by step and `to_csv` for about 30 minutes, then Plotly (`px.line`, `px.box`) for about 15 |
| 11:00 (30 min) | 3. Is it a trend? | `np.polyfit`; 1853 vs 1970; `linregress`: standard error, p-value, r²; distance from the trend as a z-score |
| 11:30 (15 min) | Break | |
| 11:45 (35 min) | 4. A second station | `load_station()`, `check_station()`, Lerwick fails, the coerce trap, the fix, `concat`, `groupby` |
| 12:20 (30 min) | 5. Combining and resampling | `unstack`, `.corr()` and `px.scatter`, `merge` (inner vs left), the Oxford–Lerwick gap, `resample` to years and seasons |
| 12:50 (10 min) | 6. Wrap | The answer; reproducibility checklist; uv demo; where next |
