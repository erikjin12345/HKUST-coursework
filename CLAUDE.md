# CLAUDE.md

Guidance for Claude Code when working in this repository (HKUST coursework, autumn 2026).

## What this repo is

Coursework for four HKUST courses. One folder per course, each with `code/` (notebooks, scripts, data), `pdf/` (slides, problem sets, solutions, exported submissions), `html/` (standalone HTML pages with typeset derivations) and a `CHEATSHEET.md` (formula sheet with page references to the lecture notes or textbook). `web/` is a small React app that renders the repo's Markdown with LaTeX in a browser. Communication with the user is in Swedish; code, comments in notebooks and assignment text are in English.

```
FINA 2203/   Fundamentals of Business Finance   (Berk & DeMarzo, Corporate Finance 6e GE)
MATH 4432/   Statistical Machine Learning        (ISLP; course tutorial repo as submodule under code/)
MATH 4511/   Quantitative Methods for Fixed Income Securities
MATH 4515/   Statistical methods for model construction
misc/        small tests
web/         Vite + React + TypeScript + Tailwind + KaTeX Markdown viewer
```

Textbooks live outside the repo in `../HKUST books/` (ISLP, Corporate Finance). Lecture PDFs are in each course's `pdf/`.

## Environment

- **Python:** `.venv/` in the repo root (Python 3.14, Homebrew). Registered as the Jupyter kernel **HKUST (.venv)** (`kernelspec` name `hkust`). Has numpy, pandas, scipy, matplotlib, seaborn, scikit-learn, statsmodels, ISLP, jupyter, nbconvert.
  - Run scripts with `.venv/bin/python`, notebooks with `--ExecutePreprocessor.kernel_name=hkust`.
  - Anaconda `base` (`~/anaconda3/bin/python`) also works and additionally has playwright/Chromium for `nbconvert --to webpdf`. Homebrew `python3` lacks scipy and sklearn; do not use it for course code.
- **Node:** Homebrew node 25, npm 11. Only `web/` uses it.
- No LaTeX installation. PDF from notebooks goes through `--to webpdf` (Chromium), not `--to pdf`.

## Common commands

```bash
# Execute a notebook in place and export HTML / PDF next to it
.venv/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel_name=hkust "<course>/code/X.ipynb"
.venv/bin/jupyter nbconvert --to html --execute --ExecutePreprocessor.kernel_name=hkust "<course>/code/X.ipynb"
~/anaconda3/bin/jupyter nbconvert --to webpdf --execute --ExecutePreprocessor.kernel_name=hkust --output-dir "<course>/pdf" "<course>/code/X.ipynb"

# Markdown + LaTeX viewer (opens http://localhost:8010)
cd web && npm install && npm run dev
cd web && npm run build          # type-check + production build

# Submodule after a fresh clone
git submodule update --init
```

## Showing math to the user

The terminal cannot render LaTeX. When a derivation or a set of formulas is easier to read typeset:

1. Write a Markdown file to `web/content/<topic>.md` using `$...$` and `$$...$$` (KaTeX, `aligned` supported, GFM tables).
2. Start `cd web && npm run dev` if it is not running; the page appears under **Scratch** in the sidebar at `http://localhost:8010/#/scratch/<topic>.md`.
3. The viewer also lists every `*.md` in the repo (cheat sheets, assignment write-ups) grouped by course. Relative image paths in those files resolve through the dev server's `/repo/` route.

Keep scratch pages short and delete them when they are no longer useful; they are committed like any other file.

## Conventions

- **Where files go:** notebooks and data in `code/`, submissions and slides in `pdf/`, standalone HTML pages in `html/` (linked from that folder's `index.html`; scripts behind their numbers in `code/html_checks/`), formula sheets as `<course>/CHEATSHEET.md`, assignment problem statements as `<course>/Assignment<N>.md`. Course folder names contain a space (`MATH 4511`); always quote paths.
- **Cheat sheets** are in Swedish, cite page numbers "(s. N)" of the source PDF, and include a facit table with numbers from worked examples or assignments so results can be verified. Follow the structure of `MATH 4511/CHEATSHEET.md`.
- **Notebooks:** one Markdown header per exercise and sub-question; interpretation cells in English under each result; all imports in the first cell; no `savefig` calls; re-run top to bottom (Restart & Run All) before export so outputs are fresh. Prefer `brentq` over hand-written Newton/grid search for root finding.
- **Verify before asserting.** When checking the user's code or reporting a numeric answer, recompute it (small `.venv/bin/python -c` script) rather than estimating. Show the comparison as a short table.
- **Assignments are the user's work.** Explain, point out errors and give corrected snippets; do not write complete solutions unless asked. Course submissions for MATH 4511 must be hand-written; code is a complement.
- **Git:** commit only when asked. Do not commit files over ~10 MB (images from the phone are 33 MB each; downscale to ~1500 px JPEG first). `node_modules/`, `dist/`, `.venv/` and checkpoints are ignored. Commit messages in Swedish, imperative, with the course code as prefix, e.g. `MATH 4511: lägg till Assignment 1`.
- **Do not touch** the submodule under `MATH 4432/code/MATH-4432-Statistical-Machine-Learning/`; it is the course's official repo.

## Memory of recurring pitfalls

- Functions that reference a global (`r`, `T`, `cash_flows`) instead of their parameter silently use a stale value from another cell. Suggest Restart Kernel + run the single cell to expose it as `NameError`.
- Rates: annual effective vs nominal (`(1+i)^t` vs `(1+i/m)^(mt)`); modified duration divides by `1+i` or `1+i^(m)/m` accordingly. Forward/FRA rates quoted annual effective must be converted to the period rate before `N(1+K)`.
- Perpetuity `C/r` is the value one period before the first payment.
- `pd.cut` on percentages needs percentage cut points; ISLP's `[0, 0.5, 1]` for `Top10perc` is wrong.
