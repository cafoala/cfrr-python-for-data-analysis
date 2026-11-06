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
- Learners on Python 3.10 have pandas 2.3; anyone on Python 3.11 or later who installed recently has pandas 3. Text columns show as `object` rather than `str`, and one error message is worded differently (Day 1, block 4).

## While live coding

- Type, don't paste. Typing sets a pace learners can follow, and your typos show them how to read errors.
- Say each line out loud as you type it, then run it.
- Run often: after every line or two when building a chart.
- Cells that are filled in already (setup, and a few cells of fiddly syntax) are for running and talking through, not typing.
- Walk round, or ask a helper to, and look for red sticky notes. When someone falls behind, point them to the solutions notebook rather than waiting for them.
- Slow down at the moments marked **Slow down** in the demo notebooks. They are the point of the block, not an obstacle to it.
- Copilot and chatbots will offer learners code. Say so openly. On both days the story stops to check a suggested fix (`errors="coerce"`) and finds it wrong.
- Day 1's practice block is the one time learners write code on their own. Stop typing, walk round, and only take answers on screen once most people have tried a few questions.

## Day 1: getting to know the data

Learners start in `day1.ipynb`, in the folder they extracted from the zip.

| Time | Block | Live-code |
|---|---|---|
| 10:00 (10 min) | 1. Welcome, the question and the data | Nothing. The question, then talk through "Meet the data" |
| 10:10 (10 min) | 2. First look at the raw file | The setup cell; open the raw file and find what makes it awkward; the naive `read_csv` |
| 10:20 (20 min) | 3. Loading it properly | `sep`, then `skiprows` and `names`, read the error, add `status`, then `na_values`; anatomy of a DataFrame |
| 10:40 (20 min) | 4. The asterisk problem | `dtypes`, find the `*` rows, `pd.to_numeric` fails loudly, the `errors="coerce"` trap, the loop, `.describe()` |
| 11:00 (10 min) | Break | |
| 11:10 (25 min) | 5. NumPy | `.to_numpy()`, loop vs vectorised, NaN, the sunshine decision |
| 11:35 (15 min) | 6. Asking questions with masks | One condition, `.loc[rows, columns]`, `&` and the missing-brackets trap, `\|`, `~`, `.isin()`, `.between()` |
| 11:50 (20 min) | 7. Split-apply-combine | Datetime index, the plan in English, `groupby`, rank the Julys |
| 12:10 (10 min) | Break | |
| 12:20 (30 min) | 8. Practice | Learners work alone for about 20 minutes on 15 questions covering the whole day, then you go through two or three together |
| 12:50 (10 min) | 9. Cliffhanger | The summer ranking; three reasons a ranking is not enough |

## Day 2: answering the question

Learners start in `day2.ipynb`, in the same folder. Its first cell runs `day2_checkpoint.ipynb`, so nobody needs yesterday's notebook to work.

| Time | Block | Live-code |
|---|---|---|
| 10:00 (15 min) | 1. Recap and "Restart and run all" | `%run` the checkpoint; the hidden-state demo |
| 10:15 (45 min) | 2. Seeing it | `fig, ax` step by step for about 30 minutes, then Plotly for about 15 |
| 11:00 (25 min) | 3. Is it a trend? | `np.polyfit`; 1853 vs 1970; distance from the trend |
| 11:25 (15 min) | Break | |
| 11:40 (30 min) | 4. A second station | `load_station()`, `check_station()`, Lerwick fails, the coerce trap, the fix, `concat` |
| 12:10 (40 min) | 5. Machine learning | Same line two ways; random vs by-year split; the classifier |
| 12:50 (10 min) | 6. Wrap | The answer; reproducibility checklist; uv demo; where next |
