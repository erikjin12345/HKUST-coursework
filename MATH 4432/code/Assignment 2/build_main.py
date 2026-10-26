"""Assemble the per-exercise notebooks into MATH_4432_Assignment_2.ipynb.

Run from anywhere:  .venv/bin/python "MATH 4432/code/Assignment 2/build_main.py"
Then execute the result:
  .venv/bin/jupyter nbconvert --to notebook --execute --inplace \
      --ExecutePreprocessor.kernel_name=hkust "MATH 4432/code/Assignment 2/MATH_4432_Assignment_2.ipynb"
and export the submission file (the course requires an .html/.pdf generated from the notebook):
  .venv/bin/jupyter nbconvert --to html --execute --ExecutePreprocessor.kernel_name=hkust \
      --output-dir "MATH 4432/pdf" "MATH 4432/code/Assignment 2/MATH_4432_Assignment_2.ipynb"

The part notebooks stay the place to edit. Imports from all parts are moved to the
first cell, and a Markdown header is inserted before each sub-question, matched on
a snippet of the code cell (see insert_headers). Exercises solved by hand get a
placeholder cell.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "MATH_4432_Assignment_2.ipynb")

HANDWRITTEN = "*Handwritten solution, see the PDF.*"


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.strip("\n")}


def code(text):
    return {"cell_type": "code", "metadata": {}, "execution_count": None,
            "outputs": [], "source": text.strip("\n")}


def load_cells(name):
    path = os.path.join(HERE, name)
    if os.path.getsize(path) == 0:
        print(f"WARNING: {name} is empty on disk (not saved?)")
        return []
    with open(path) as f:
        nb = json.load(f)
    cells = []
    for c in nb["cells"]:
        src = "".join(c["source"]) if isinstance(c["source"], list) else c["source"]
        if src.strip():
            cells.append(md(src) if c["cell_type"] == "markdown" else code(src))
    return cells


IMPORT_RE = re.compile(r"^(import \S|from \S+ import )")


def split_imports(cells):
    """Remove top-level import lines from code cells and return them in order."""
    imports = []
    for c in cells:
        if c["cell_type"] != "code":
            continue
        keep = []
        for line in c["source"].splitlines():
            if IMPORT_RE.match(line):
                imports.append(line.rstrip())
            else:
                keep.append(line)
        c["source"] = "\n".join(keep).strip("\n")
    return [c for c in cells if c["source"].strip()], imports


def insert_headers(cells, headers):
    """Insert a Markdown cell before the first code cell whose source contains each key."""
    out, used = [], set()
    for c in cells:
        for key, header in headers.items():
            if key not in used and c["cell_type"] == "code" and key in c["source"]:
                out.append(md(header))
                used.add(key)
                break
        out.append(c)
    for key in headers.keys() - used:
        print(f"WARNING: no cell contains {key!r}; header not inserted")
    return out


# ---------------------------------------------------------------------------
# Parts
# ---------------------------------------------------------------------------
ex13 = load_cells("ch4_ex_13.ipynb")
ex13 = [c for c in ex13 if not c["source"].startswith("# Assignment 2")]   # old title cell

ex14 = load_cells("ch4_ex_14.ipynb")
if not ex14:
    ex14 = [md("## Chapter 4, Exercise 14\n\n*TODO: `ch4_ex_14.ipynb` was empty when this file was built.*")]
else:
    ex14 = insert_headers(ex14, {
        'Auto["mpg01"] =': "## Chapter 4, Exercise 14\n\n### (a)–(b) The variable `mpg01` and its association with the other features",
        "train, test = train_test_split(": "### (c)–(h) Training and test sets; LDA, QDA, logistic regression, naive Bayes and KNN",
    })

ex2 = insert_headers(load_cells("ch5_ex_2.ipynb"), {
    "probs = {}": "### (g) Probability that the $j$th observation is in the bootstrap sample, $n = 1, \\dots, 100\\,000$",
    "store = np.empty": "### (h) Simulation with $n = 100$ and $j = 4$",
})

ex56 = insert_headers(load_cells("ch5_ex_5_6.ipynb"), {
    "Default = load_data": "## Chapter 5, Exercise 5\n\n### (a) Logistic regression of `default` on `income` and `balance`",
    "# Split the data": "### (b) Validation set approach",
    "# Repeat this three times": "### (c) Three different splits",
    "# Logistic regression with dummy": "### (d) Adding a dummy variable for `student`",
    'MS(["income", "balance"]).fit_transform(Default)': "## Chapter 5, Exercise 6\n\n### (a) Standard errors from `sm.GLM()`",
    "def boot_fn": "### (b) The function `boot_fn()`",
    "def boot_SE": "### (c) Bootstrap standard errors",
    '"sm.GLM SE"': "### (d) Comparison of the standard errors",
})

ex13, imp13 = split_imports(ex13)
ex14, imp14 = split_imports(ex14)
ex2, imp2 = split_imports(ex2)
ex56, imp56 = split_imports(ex56)

imports = list(dict.fromkeys(imp13 + imp14 + imp2 + imp56))   # dedupe, keep order

cells = [
    md("# MATH 4432 – Assignment 2\n\n"
       "Chapter 4: exercises 1, 2, 3, 13, 14. Chapter 5: exercises 1, 2, 5, 6.\n\n"
       "Exercises 4.1–4.3, 5.1 and 5.2 (a)–(f) are solved by hand."),
    code("\n".join(imports) + '\n\n%config InlineBackend.figure_format = "retina"'),
    md("## Chapter 4, Exercise 1\n\n" + HANDWRITTEN),
    md("## Chapter 4, Exercise 2\n\n" + HANDWRITTEN),
    md("## Chapter 4, Exercise 3\n\n" + HANDWRITTEN),
    *ex13,
    *ex14,
    md("## Chapter 5, Exercise 1\n\n" + HANDWRITTEN),
    md("## Chapter 5, Exercise 2\n\n### (a)–(f)\n\n" + HANDWRITTEN),
    *ex2,
    *ex56,
]

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "HKUST (.venv)", "language": "python", "name": "hkust"},
        "language_info": {"name": "python"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}
for i, c in enumerate(nb["cells"]):
    c["id"] = f"cell-{i:03d}"

with open(OUT, "w") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print(f"wrote {os.path.relpath(OUT, HERE)} with {len(cells)} cells")
