"""Export all figures referenced in latex/Assignment1.tex to code/figures/.

Run from anywhere:  python export_figures.py
Figures are regenerated from the ISLP data sets, so the notebook does not need to be re-run.
"""
import os, shutil
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.nonparametric.smoothers_lowess import lowess
from ISLP import load_data

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "figures")
os.makedirs(OUT, exist_ok=True)


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("saved", os.path.relpath(path, HERE))


# ----------------------------------------------------------------------------
# Diagnostic plots (R's plot(lm)) for a fitted statsmodels OLS result
# ----------------------------------------------------------------------------
def diagnostic_plots(results, n_label=3):
    infl = results.get_influence()
    fitted, resid = results.fittedvalues, results.resid
    std_resid = infl.resid_studentized_internal
    leverage, cooks = infl.hat_matrix_diag, infl.cooks_distance[0]
    p, n = results.df_model + 1, len(resid)
    idx = results.model.data.row_labels
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    ax = axes[0, 0]
    ax.scatter(fitted, resid, alpha=0.5)
    s = lowess(resid, fitted, frac=0.6); ax.plot(s[:, 0], s[:, 1], "r-")
    ax.axhline(0, color="grey", ls="--")
    ax.set(xlabel="Fitted values", ylabel="Residuals", title="Residuals vs Fitted")
    for i in np.argsort(np.abs(resid.values))[-n_label:]:
        ax.annotate(str(idx[i]), (fitted.iloc[i], resid.iloc[i]), fontsize=8)

    ax = axes[0, 1]
    (osm, osr), (slope, intercept, _) = stats.probplot(std_resid, dist="norm")
    ax.scatter(osm, osr, alpha=0.5); ax.plot(osm, slope * osm + intercept, "r-")
    ax.set(xlabel="Theoretical quantiles", ylabel="Standardized residuals", title="Normal Q-Q")

    ax = axes[1, 0]
    sqrt_abs = np.sqrt(np.abs(std_resid))
    ax.scatter(fitted, sqrt_abs, alpha=0.5)
    s = lowess(sqrt_abs, fitted, frac=0.6); ax.plot(s[:, 0], s[:, 1], "r-")
    ax.set(xlabel="Fitted values", ylabel=r"$\sqrt{|\mathrm{std.\ residuals}|}$", title="Scale-Location")

    ax = axes[1, 1]
    ax.scatter(leverage, std_resid, alpha=0.5)
    ax.axhline(0, color="grey", ls="--")
    ax.axvline(2 * p / n, color="grey", ls=":", label="2p/n")
    lev = np.linspace(leverage.min(), leverage.max(), 100)
    for d in (0.5, 1.0):
        for sign in (1, -1):
            ax.plot(lev, sign * np.sqrt(d * p * (1 - lev) / lev), "r--", lw=0.8)
    ax.set_ylim(std_resid.min() - 0.5, std_resid.max() + 0.5)
    ax.set(xlabel="Leverage", ylabel="Standardized residuals", title="Residuals vs Leverage")
    for i in np.argsort(cooks)[-n_label:]:
        ax.annotate(str(idx[i]), (leverage[i], std_resid[i]), fontsize=8)
    ax.legend()
    fig.tight_layout()
    return fig


# ============================================================================
# Chapter 2, Exercise 8 -- College
# ============================================================================
college = load_data("College")
college["Elite"] = pd.cut(college["Top10perc"], [0, 50, 100], labels=["No", "Yes"])

# 8(d) scatterplot matrix
axes = pd.plotting.scatter_matrix(college[["Top10perc", "Apps", "Enroll"]], figsize=(8, 8), alpha=0.5)
save(axes[0, 0].get_figure(), "college_scatter_matrix.png")

# 8(e)-(f) boxplots of Outstate by Private and by Elite
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
college.boxplot(column="Outstate", by="Private", ax=axes[0]); axes[0].set_title("Outstate vs Private")
college.boxplot(column="Outstate", by="Elite", ax=axes[1]);   axes[1].set_title("Outstate vs Elite")
for ax in axes: ax.set_ylabel("Out-of-state tuition")
fig.suptitle(""); fig.tight_layout()
save(fig, "college_boxplots.png")

# 8(g) histograms with different bin counts
fig, axes = plt.subplots(2, 2, figsize=(11, 8))
for ax, (col, bins) in zip(axes.ravel(), [("Apps", 50), ("Enroll", 30), ("Outstate", 20), ("Grad.Rate", 15)]):
    ax.hist(college[col], bins=bins, edgecolor="k")
    ax.set(title=f"{col} ({bins} bins)", xlabel=col, ylabel="count")
fig.tight_layout()
save(fig, "college_hist.png")

# ============================================================================
# Chapter 2, Exercise 10 -- Boston
# ============================================================================
Boston = load_data("Boston")

# 10(c) scatterplots with point size = number of tracts at the same coordinates
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
pairs = [("tax", "rad", "Property-tax rate", "Accessibility to radial highways"),
         ("lstat", "medv", "Lower status of population (%)", "Median home value"),
         ("indus", "nox", "Non-retail business acres (%)", "NOx concentration"),
         ("medv", "ptratio", "Median home value", "Pupil-teacher ratio")]
for ax, (x, y, xlab, ylab) in zip(axes.ravel(), pairs):
    counts = Boston.groupby([x, y]).size().reset_index(name="n")
    ax.scatter(counts[x], counts[y], s=8 + 4 * counts["n"], alpha=0.4, edgecolor="k", linewidth=0.3)
    for _, r in counts[counts["n"] >= 20].iterrows():
        ax.annotate(f"n={int(r['n'])}", (r[x], r[y]), textcoords="offset points", xytext=(8, -12), fontsize=8)
    ax.set_xlabel(xlab); ax.set_ylabel(ylab); ax.set_title(f"{y} vs {x}", fontsize=10)
fig.tight_layout()
save(fig, "boston_scatter.png")

# 10(d) correlation with crime
corr_crime = Boston.corr()["crim"].drop("crim").sort_values()
fig, ax = plt.subplots(figsize=(8, 5))
corr_crime.plot.barh(ax=ax)
ax.set_xlabel("Correlation with crim"); ax.axvline(0, color="black", linewidth=0.8)
fig.tight_layout()
save(fig, "crime_corr.png")

# 10(e) histograms of crim, tax, ptratio
fig, axes = plt.subplots(1, 3, figsize=(14, 4))
for ax, col in zip(axes, ["crim", "tax", "ptratio"]):
    ax.hist(Boston[col], bins=30, edgecolor="k")
    ax.set_title(f"{col}  (range {Boston[col].min():.2f} - {Boston[col].max():.2f})", fontsize=10)
    ax.set_xlabel(col); ax.set_ylabel("count")
fig.tight_layout()
save(fig, "boston_hist.png")

# ============================================================================
# Chapter 3, Exercise 1 -- Table 3.4 (copy the screenshot if present, else render it)
# ============================================================================
src = os.path.join(HERE, "table3.4.png")
if os.path.exists(src):
    shutil.copy(src, os.path.join(OUT, "table3.4.png")); print("copied figures/table3.4.png")
else:
    rows = [["Intercept", "2.939", "0.3119", "9.42", "< 0.0001"],
            ["TV", "0.046", "0.0014", "32.81", "< 0.0001"],
            ["radio", "0.189", "0.0086", "21.89", "< 0.0001"],
            ["newspaper", "-0.001", "0.0059", "-0.18", "0.8599"]]
    fig, ax = plt.subplots(figsize=(7, 2)); ax.axis("off")
    t = ax.table(cellText=rows, colLabels=["", "Coefficient", "Std. error", "t-statistic", "p-value"], loc="center")
    t.auto_set_font_size(False); t.set_fontsize(10); t.scale(1, 1.4)
    save(fig, "table3.4.png")

# ============================================================================
# Chapter 3, Exercise 8 -- simple linear regression
# ============================================================================
auto = load_data("Auto")
X1 = sm.add_constant(auto["horsepower"].astype(float))
lin_reg = sm.OLS(auto["mpg"], X1).fit()

# 8(b) scatter with least squares line
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(auto["horsepower"], auto["mpg"], alpha=0.5)
ax.axline((0, lin_reg.params["const"]), slope=lin_reg.params["horsepower"], color="r", linestyle="--", linewidth=2)
ax.set(xlabel="horsepower", ylabel="mpg", title="mpg vs horsepower with least squares line")
save(fig, "auto_fit_line.png")

# 8(c) standard diagnostic plots
save(diagnostic_plots(lin_reg), "auto_diag_simple.png")

# 8(c) binned mean residual and binned spread
x, err = auto["horsepower"], lin_reg.resid
bins = pd.qcut(x, 10)
g = err.groupby(bins, observed=True)
summ = pd.DataFrame({"center": x.groupby(bins, observed=True).mean(), "mean": g.mean(), "sd": g.std(), "n": g.size()})
summ["se"] = summ["sd"] / np.sqrt(summ["n"])
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
axes[0].scatter(x, err, alpha=0.2, color="grey")
axes[0].errorbar(summ["center"], summ["mean"], yerr=2 * summ["se"], fmt="o-", color="k", capsize=3)
axes[0].axhline(0, color="r", ls="--")
axes[0].set(xlabel="horsepower", ylabel="residual", title="Binned mean residual +/- 2 SE")
axes[1].plot(summ["center"], summ["sd"], "o-")
axes[1].set(xlabel="horsepower", ylabel="residual SD", title="Residual spread per bin")
fig.tight_layout()
save(fig, "binned_mean_res.png")

# ============================================================================
# Chapter 3, Exercise 9 -- multiple linear regression
# ============================================================================
num = auto.select_dtypes("number")

# 9(a) scatterplot matrix of all variables
axes = pd.plotting.scatter_matrix(num, figsize=(14, 14), alpha=0.3, s=8)
for ax in axes.ravel():
    ax.xaxis.label.set_fontsize(8); ax.yaxis.label.set_fontsize(8)
save(axes[0, 0].get_figure(), "auto_scatter_matrix.png")

# 9(c)-(d) full model and its diagnostics
base = "mpg ~ cylinders + displacement + horsepower + weight + acceleration + year + origin"
results = ols(base, auto).fit()
save(diagnostic_plots(results), "diag_base.png")

# 9(f) log-log model and its diagnostics
loglog = ols("np.log(mpg) ~ cylinders + displacement + np.log(horsepower) + np.log(weight) + acceleration + year + origin", auto).fit()
save(diagnostic_plots(loglog), "diag_loglog.png")

print(f"\n{len(os.listdir(OUT))} files in {os.path.relpath(OUT, HERE)}/")
