"""Copy the figures from the executed MATH_4432_Assignment_2.ipynb to MATH 4432/code/figures/.

Run after executing the notebook:  .venv/bin/python "MATH 4432/code/Assignment 2/export_figures.py"
The PNGs are taken from the stored cell outputs, so the notebook itself needs no savefig calls.
A figure is named after a snippet of the code cell that produced it (see FIGURES).
"""
import base64
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
NB = os.path.join(HERE, "MATH_4432_Assignment_2.ipynb")
OUT = os.path.join(HERE, "..", "figures")

FIGURES = {
    "ax.hist(returns": "a2_weekly_hist.png",
    "vol_52w = ": "a2_weekly_returns_vol.png",
    'ax.plot(t, Weekly["Volume"])': "a2_weekly_volume.png",
    "sns.heatmap(Weekly": "a2_weekly_corr.png",
    "Auto.boxplot(": "a2_auto_boxplots.png",
    'Auto.drop(columns=["mpg"]).corr()': "a2_auto_corr.png",
    "sns.boxplot(": "a2_weekly_lag_box.png",
    "up_share = ": "a2_weekly_up_share.png",
    "probs = {}": "a2_bootstrap_prob.png",
}

os.makedirs(OUT, exist_ok=True)
with open(NB) as f:
    cells = json.load(f)["cells"]

found = set()
for c in cells:
    src = "".join(c["source"])
    pngs = [o["data"]["image/png"] for o in c.get("outputs", []) if "image/png" in o.get("data", {})]
    if not pngs:
        continue
    names = [name for key, name in FIGURES.items() if key in src]
    if len(names) != 1 or len(pngs) != 1:
        print(f"WARNING: cell with {len(pngs)} figure(s) matched {names}; skipped:\n  {src.splitlines()[0]}")
        continue
    with open(os.path.join(OUT, names[0]), "wb") as f:
        f.write(base64.b64decode(pngs[0]))
    found.add(names[0])
    print("saved figures/" + names[0])

for name in sorted(set(FIGURES.values()) - found):
    print(f"WARNING: {name} not found in the notebook outputs")
