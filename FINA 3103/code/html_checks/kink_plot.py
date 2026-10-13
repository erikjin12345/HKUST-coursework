"""Kinked CAL and kinked utility U(y) for HW1 Part B (c).

Writes two PNGs to web/content/knackt-cal/ and prints the numbers used
on the scratch page web/content/knackt-cal.md.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

mu = np.array([0.10, 0.06])
sd = np.array([0.18, 0.10])
rho = 0.25
Sigma = np.array([[sd[0]**2, rho*sd[0]*sd[1]], [rho*sd[0]*sd[1], sd[1]**2]])
r_f, r_b = 0.03, 0.06

z = np.linalg.solve(Sigma, mu - r_f)
w = z / z.sum()
E_P = w @ mu
var_P = w @ Sigma @ w
sd_P = np.sqrt(var_P)
A_lo = (E_P - r_b) / var_P
A_hi = (E_P - r_f) / var_P
print(f"w* = {w.round(4)}, E_P = {E_P:.4f}, sd_P = {sd_P:.4f}, var_P = {var_P:.6f}")
print(f"slope lend = {(E_P-r_f)/sd_P:.4f}, slope borrow = {(E_P-r_b)/sd_P:.4f}")
print(f"A range for y = 1: [{A_lo:.4f}, {A_hi:.4f}]")


def y_opt(A):
    y_L = (E_P - r_f) / (A * var_P)
    y_B = (E_P - r_b) / (A * var_P)
    if y_L <= 1:
        return y_L
    if y_B >= 1:
        return y_B
    return 1.0


def U(y, A):
    r = np.where(y <= 1, r_f, r_b)
    return r + y * (E_P - r) - 0.5 * A * var_P * y**2


cases = [("lånar ut", 6.0), ("i knäcken", 3.0), ("lånar", 1.2)]
for name, A in cases:
    y_L = (E_P - r_f) / (A * var_P)
    y_B = (E_P - r_b) / (A * var_P)
    y = y_opt(A)
    print(f"A = {A}: y_L = {y_L:.4f}, y_B = {y_B:.4f}, y* = {y:.4f}, "
          f"U* = {U(np.array(y), A):.5f}")
print(f"dU/dy at y=1-: {E_P - r_f:.4f} - A*{var_P:.6f}; "
      f"at y=1+: {E_P - r_b:.4f} - A*{var_P:.6f}; jump = {r_b - r_f:.2f}")

out = Path(__file__).resolve().parents[3] / "web" / "content" / "knackt-cal"
out.mkdir(parents=True, exist_ok=True)
colors = ["#1f77b4", "#9a3b1e", "#2ca02c"]

# Figure 1: U(y) for three investors
fig, ax = plt.subplots(figsize=(7, 4.2))
ys = np.linspace(0, 2.2, 600)
for (name, A), c in zip(cases, colors):
    ax.plot(ys, U(ys, A), color=c, label=f"A = {A} ({name})")
    # smooth parabolas that U follows on each side
    ax.plot(ys, r_f + ys*(E_P-r_f) - 0.5*A*var_P*ys**2, color=c, lw=0.8, ls=":")
    ax.plot(ys, r_b + ys*(E_P-r_b) - 0.5*A*var_P*ys**2, color=c, lw=0.8, ls="--")
    y = y_opt(A)
    ax.plot(y, U(np.array(y), A), "o", color=c)
ax.axvline(1, color="grey", lw=0.8)
ax.set_xlabel("y (andel i P*)")
ax.set_ylabel("U(y)")
ax.set_ylim(0.025, 0.075)
ax.set_title("U(y) är kontinuerlig men har en knäck i y = 1")
ax.legend(fontsize=8, loc="lower left")
fig.tight_layout()
fig.savefig(out / "utility.png", dpi=150)

# Figure 2: kinked CAL and indifference curves in (sigma, E) plane
fig, ax = plt.subplots(figsize=(7, 4.2))
s = np.linspace(0, 0.25, 400)
ax.plot(s, r_f + (E_P-r_f)/sd_P*s, color="grey", lw=0.8, ls=":")
ax.plot(s, r_b + (E_P-r_b)/sd_P*s, color="grey", lw=0.8, ls=":")
cal = np.where(s <= sd_P, r_f + (E_P-r_f)/sd_P*s, r_b + (E_P-r_b)/sd_P*s)
ax.plot(s, cal, color="black", lw=2, label="knäckt CAL")
ax.plot(sd_P, E_P, "ks")
ax.annotate("P*", (sd_P, E_P), xytext=(5, -12), textcoords="offset points")
for (name, A), c in zip(cases, colors):
    y = y_opt(A)
    Uy = float(U(np.array(y), A))
    ax.plot(s, Uy + 0.5*A*s**2, color=c, lw=1, label=f"indifferens, A = {A}")
    r = r_f if y <= 1 else r_b
    ax.plot(y*sd_P, r + y*(E_P-r), "o", color=c)
ax.set_xlim(0, 0.25)
ax.set_ylim(0.02, 0.12)
ax.set_xlabel("σ")
ax.set_ylabel("E[r]")
ax.set_title("Lutning 0.4417 till vänster om P*, 0.1684 till höger")
ax.legend(fontsize=8, loc="upper left")
fig.tight_layout()
fig.savefig(out / "cal.png", dpi=150)
print("saved to", out)

# Figure 3: y*(A) is a function of A with a flat part at y = 1
fig, ax = plt.subplots(figsize=(7, 4.2))
As = np.linspace(0.4, 10, 800)
yL = (E_P - r_f) / (As * var_P)
yB = (E_P - r_b) / (As * var_P)
ys_opt = np.array([y_opt(a) for a in As])
ax.plot(As, yL, color=colors[0], lw=1, ls=":", label="y_L (om allt gick till 3 %)")
ax.plot(As, yB, color=colors[2], lw=1, ls="--", label="y_B (om allt gick till 6 %)")
ax.plot(As, ys_opt, color="black", lw=2, label="y*(A)")
ax.axhline(1, color="grey", lw=0.8)
for a in (A_lo, A_hi):
    ax.axvline(a, color="grey", lw=0.8, ls="--")
ax.axvspan(A_lo, A_hi, color=colors[1], alpha=0.08)
ax.text(0.95, 0.25, "lånar", ha="center")
ax.text((A_lo+A_hi)/2, 2.7, "knäcken\ny* = 1", ha="center", va="top")
ax.text(7, 2.7, "lånar ut", ha="center")
for name, a in (("Chen", 1.5), ("Elaine", 3.0)):
    ax.plot(a, y_opt(a), "o", color=colors[1])
    ax.annotate(name, (a, y_opt(a)), xytext=(4, -14), textcoords="offset points")
ax.set_xlim(0.4, 10)
ax.set_ylim(0, 3)
ax.set_xlabel("A")
ax.set_ylabel("y")
ax.set_title(f"y*(A): platt på y = 1 för {A_lo:.4f} ≤ A ≤ {A_hi:.4f}")
ax.legend(fontsize=8, loc="center right")
fig.tight_layout()
fig.savefig(out / "y_of_A.png", dpi=150)
print("y*(1.5) =", round(y_opt(1.5), 4), " y*(3) =", y_opt(3.0))
