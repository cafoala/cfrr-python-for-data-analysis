# Instructor notes

The course is taught as a code-along: you type into a blank notebook on the projector, and learners type the same code into blank notebooks of their own.

Your script is the pair of **demo notebooks** in `instructor/`. Each one is the complete notebook plus speaker-note cells, set off as quotes, saying what to say, what to ask, where to slow down, the misconceptions to watch for, and the answer to every Predict prompt. Numbers in the notes come from the data snapshot of 29 October 2026. If you change the snapshot, rerun the demo notebooks and update the notes.

Learners get the **solutions notebooks** in `notebooks/`: the same notebooks without the speaker notes. They read them on GitHub, and if they fall behind, they copy the cell they missed from there.

Learners don't need git or a copy of this repository. They work in the course folder from the CfRR setup, and the first cell of each day downloads what it needs.

## Before each session

- Restart the kernel of the demo notebook. Hidden state catches instructors too.
- Project a fresh notebook in an empty folder, not the demo notebook, so your screen matches theirs. Keep the demo notebook on a second screen, a tablet or paper.
- Check the room has internet. The demo notebooks say what to do if a download fails.
- Zoom JupyterLab to about 150% (Ctrl or Cmd and `+`) and use a light theme.
- Hand out two colours of sticky note: green for "done", red for "stuck, please come over".
- Learners on Python 3.10 have pandas 2.3; anyone on Python 3.11 or later who installed recently has pandas 3. Text columns show as `object` rather than `str`, and one error message is worded differently (Day 1, block 4).

## While live coding

- Type, don't paste. Typing sets a pace learners can follow, and your typos show them how to read errors.
- Say each line out loud as you type it, then run it.
- Run often: after every line or two when building a chart.
- For an exercise, copy its prompt cell from the demo notebook into your live notebook so it is on screen. Give learners 3 to 5 minutes, then do it yourself. Walk round, or ask a helper to, and look for red sticky notes.
- When someone falls behind, point them to the solutions notebook rather than waiting for them.
- Slow down at the moments marked **Slow down** in the demo notebooks. They are the point of the block, not an obstacle to it.
- Copilot and chatbots will offer learners code. Say so openly. Several exercises ask learners to check a suggestion rather than write code from scratch.

## Day 1: getting to know the data

Learners start in a blank `day1.ipynb` in their course folder.

| Time | Block | Live-code |
|---|---|---|
| 10:00 (15 min) | 1. Welcome, the question and the data | Nothing. Show of hands and a written guess, then talk through "Meet the data" |
| 10:15 (15 min) | 2. First look at the raw file | Imports and the download; print the first and last lines; the naive `read_csv` |
| 10:30 (30 min) | 3. Loading it properly | `sep`, then `skiprows` and `names`, read the error, add `status`, `na_values`; anatomy of a DataFrame |
| 11:00 (30 min) | 4. The asterisk problem | `dtypes`, find the `*` rows, the `errors="coerce"` trap, the loop |
| 11:30 (15 min) | Break | |
| 11:45 (35 min) | 5. NumPy | `.to_numpy()`, loop vs vectorised, NaN, masks, the sunshine decision |
| 12:20 (30 min) | 6. Split-apply-combine | Datetime index, Describe first, `groupby`, rank the Julys |
| 12:50 (10 min) | 7. Cliffhanger | The summer ranking; three reasons a ranking is not enough |

## Day 2: answering the question

Learners start in a blank `day2.ipynb` in the same folder. Its first cell downloads and runs `day2_checkpoint.ipynb`, so nobody needs yesterday's notebook to work.

| Time | Block | Live-code |
|---|---|---|
| 10:00 (15 min) | 1. Recap and "Restart and run all" | Download and `%run` the checkpoint; the hidden-state demo |
| 10:15 (45 min) | 2. Seeing it | `fig, ax` step by step for about 30 minutes, then Plotly for about 15 |
| 11:00 (25 min) | 3. Is it a trend? | `np.polyfit`; 1853 vs 1970; distance from the trend |
| 11:25 (15 min) | Break | |
| 11:40 (30 min) | 4. A second station | `load_station()`, `check_station()`, Lerwick fails, the coerce trap, the fix, `concat` |
| 12:10 (40 min) | 5. Machine learning | Same line two ways; random vs by-year split; the classifier |
| 12:50 (10 min) | 6. Wrap | The answer; reproducibility checklist; uv demo; where next |
