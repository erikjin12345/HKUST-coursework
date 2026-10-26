"""Bias-variance trade-off simulation (extra coding exercise, Assignment 1).

Regenerates the three figures used in the report into code/figures/:
    bv_mse.png          MSE vs 1/K for KNN with linear regression as reference, one panel per p
    bv_knn_decomp.png   bias^2, variance and MSE of KNN vs 1/K, one panel per p
    bv_lm.png           bias^2, variance and MSE of linear regression vs p
and prints the result tables. Run:  python export_bv_figures.py
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "figures")
os.makedirs(OUT, exist_ok=True)

np.random.seed(0)
ntrain, ntest, nrep, p, sigma = 50, 500, 100, 20, 0.5
puse = np.array([1, 2, 3, 4, 10, 20])
k = np.arange(1, 10)

Xtrain = np.random.uniform(-1, 1, [ntrain, p])
Xtest = np.random.uniform(-1, 1, [ntest, p])
y0 = np.sin(2 * Xtrain[:, 0])          # only the first predictor matters
ytest = np.sin(2 * Xtest[:, 0])         # noise-free truth on the test set

out_lm, out_knn = pd.DataFrame(), pd.DataFrame()
for i in range(len(puse)):
    cols = slice(0, puse[i])
    yhat_lm = np.zeros((ntest, nrep))
    yhat_knn = np.zeros((ntest, nrep, len(k)))
    for l in range(nrep):
        y = y0 + np.random.normal(0, sigma, ntrain)
        yhat_lm[:, l] = LinearRegression().fit(Xtrain[:, cols], y).predict(Xtest[:, cols])
        for j in range(len(k)):
            yhat_knn[:, l, j] = KNeighborsRegressor(k[j]).fit(Xtrain[:, cols], y).predict(Xtest[:, cols])

    ybar = yhat_lm.mean(axis=1)
    out_lm = pd.concat([out_lm, pd.DataFrame({
        "biasSQ_lm": [np.mean((ytest - ybar) ** 2)],
        "variance_lm": [np.mean((yhat_lm - ybar[:, None]) ** 2)],
        "MSE": [np.mean((yhat_lm - ytest[:, None]) ** 2)],
        "p": [puse[i]]})])
    for j in range(len(k)):
        yh = yhat_knn[:, :, j]
        ybar = yh.mean(axis=1)
        out_knn = pd.concat([out_knn, pd.DataFrame({
            "biasSQ_knn": [np.mean((ytest - ybar) ** 2)],
            "variance_knn": [np.mean((yh - ybar[:, None]) ** 2)],
            "MSE": [np.mean((yh - ytest[:, None]) ** 2)],
            "1/K": [1 / k[j]], "K": [k[j]], "p": [puse[i]]})])
out_lm = out_lm.reset_index(drop=True)
out_knn = out_knn.reset_index(drop=True)


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("saved figures/" + name)


# Figure 1: MSE vs 1/K (ISLR Figure 3.20 style)
fig, axes = plt.subplots(2, 3, figsize=(13, 7), sharex=True, sharey=True)
for ax, pv in zip(axes.ravel(), puse):
    d = out_knn[out_knn["p"] == pv].sort_values("1/K")
    lm = out_lm.loc[out_lm["p"] == pv, "MSE"].iloc[0]
    ax.plot(d["1/K"], d["MSE"], "o-", color="green", label="KNN")
    ax.axhline(lm, color="k", ls="--", label="Linear regression")
    ax.set_xscale("log"); ax.set_title(f"p = {pv}")
    ax.set_xlabel("1/K"); ax.set_ylabel("Mean squared error")
axes[0, 0].legend(); fig.tight_layout()
save(fig, "bv_mse.png")

# Figure 2: KNN decomposition
fig, axes = plt.subplots(2, 3, figsize=(13, 7), sharex=True, sharey=True)
for ax, pv in zip(axes.ravel(), puse):
    d = out_knn[out_knn["p"] == pv].sort_values("1/K")
    ax.plot(d["1/K"], d["biasSQ_knn"], "o-", label="Bias$^2$")
    ax.plot(d["1/K"], d["variance_knn"], "s-", label="Variance")
    ax.plot(d["1/K"], d["MSE"], "k^-", label="MSE")
    ax.set_xscale("log"); ax.set_title(f"KNN, p = {pv}"); ax.set_xlabel("1/K")
axes[0, 0].legend(); fig.tight_layout()
save(fig, "bv_knn_decomp.png")

# Figure 3: linear regression decomposition vs p
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(out_lm["p"], out_lm["biasSQ_lm"], "o-", label="Bias$^2$")
ax.plot(out_lm["p"], out_lm["variance_lm"], "s-", label="Variance")
ax.plot(out_lm["p"], out_lm["MSE"], "k^-", label="MSE")
ax.set(xlabel="p", ylabel="error", title="Linear regression"); ax.legend()
fig.tight_layout()
save(fig, "bv_lm.png")

pd.set_option("display.width", 200)
print("\nLinear regression:"); print(out_lm.round(4).to_string(index=False))
print("\nKNN MSE (rows: p, columns: K):"); print(out_knn.pivot(index="p", columns="K", values="MSE").round(3))
print("\nKNN bias^2 (rows: p, columns: K):"); print(out_knn.pivot(index="p", columns="K", values="biasSQ_knn").round(3))
print("\nKNN variance (rows: p, columns: K):"); print(out_knn.pivot(index="p", columns="K", values="variance_knn").round(3))
best = out_knn.loc[out_knn.groupby("p")["MSE"].idxmin(), ["p", "K", "MSE"]]
print("\nbest K per p:"); print(best.to_string(index=False))
print("check max|bias^2 + var - MSE| =", (out_knn["biasSQ_knn"] + out_knn["variance_knn"] - out_knn["MSE"]).abs().max())
