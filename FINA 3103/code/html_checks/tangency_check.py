"""Numbers behind html/tangency.html (FINA 3103 Assignment 1, Part B (b)).

Derives the tangency (Sharpe-maximising) portfolio of a stock fund and a bond
fund three ways: closed-form two-asset formula, w proportional to Sigma^-1 mu,
and a direct numerical maximisation of the Sharpe ratio. Also prints the SVG
coordinates used for the frontier figure.
"""
import numpy as np
from scipy.optimize import minimize_scalar

E_S, s_S = 0.10, 0.18
E_B, s_B = 0.06, 0.10
rho, rf = 0.25, 0.03

cov = rho * s_S * s_B
R_S, R_B = E_S - rf, E_B - rf  # excess returns

# 1) closed-form two-asset formula
num = R_S * s_B**2 - R_B * cov
den = R_S * s_B**2 + R_B * s_S**2 - (R_S + R_B) * cov
w_S = num / den
print(f"cov = {cov:.4f}, R_S = {R_S:.2f}, R_B = {R_B:.2f}")
print(f"numerator = {num:.6f}, denominator = {den:.6f}, w_S = {w_S:.4f}, w_B = {1-w_S:.4f}")

# 2) w proportional to Sigma^-1 mu
Sigma = np.array([[s_S**2, cov], [cov, s_B**2]])
mu = np.array([R_S, R_B])
z = np.linalg.solve(Sigma, mu)
print(f"z = Sigma^-1 mu = {z.round(4)}, normalised = {(z / z.sum()).round(4)}")

# 3) numerical maximisation of the Sharpe ratio
def sharpe(w):
    x = np.array([w, 1 - w])
    return (x @ mu) / np.sqrt(x @ Sigma @ x)
res = minimize_scalar(lambda w: -sharpe(w), bounds=(-2, 3), method="bounded")
print(f"numerical argmax w_S = {res.x:.4f}, Sharpe = {-res.fun:.4f}")

# Portfolio P* and the first-order condition Sigma w = c mu
x = np.array([w_S, 1 - w_S])
E_P = x @ np.array([E_S, E_B])
s_P = np.sqrt(x @ Sigma @ x)
print(f"E[r_P] = {E_P:.4f}, sigma_P = {s_P:.4f}, Sharpe = {(E_P - rf) / s_P:.4f}")
print(f"Sigma w = {(Sigma @ x).round(6)}, (Sigma w)/mu = {((Sigma @ x) / mu).round(4)}, "
      f"sigma_P^2/(mu'w) = {s_P**2 / (x @ mu):.4f}")

# Sharpe of some other mixes, for the table
for w in [0, 0.25, w_S, 0.75, 1]:
    print(f"  w_S = {w:.4f}: Sharpe = {sharpe(w):.4f}")

# SVG coordinates: sigma 0..0.22 -> x 60..680, E 0.02..0.12 -> y 320..20
X = lambda s: 60 + s / 0.22 * 620
Y = lambda e: 320 - (e - 0.02) / 0.10 * 300
pts = []
for w in np.linspace(-0.2, 1.2, 57):
    xx = np.array([w, 1 - w])
    pts.append(f"{X(np.sqrt(xx @ Sigma @ xx)):.1f},{Y(xx @ np.array([E_S, E_B])):.1f}")
print("frontier path: M" + " L".join(pts))
for name, s, e in [("rf", 0, rf), ("S", s_S, E_S), ("B", s_B, E_B), ("P", s_P, E_P)]:
    print(f"{name}: ({X(s):.1f}, {Y(e):.1f})")
sr = (E_P - rf) / s_P
# a worse CAL through the bond fund
sr_B = R_B / s_B
print(f"Sharpe_B = {sr_B:.4f}")
print(f"Sharpe_S = {R_S / s_S:.4f}")
s_top = (0.12 - rf) / sr  # where the CAL leaves the plot
print(f"CAL end at E=0.12: sigma = {s_top:.4f} -> ({X(s_top):.1f}, {Y(0.12):.1f})")
print(f"CAL via B end at sigma=0.22: ({X(0.22):.1f}, {Y(rf + sr_B * 0.22):.1f})")
print("axis ticks x:", [(s, round(X(s), 1)) for s in (0, 0.05, 0.10, 0.15, 0.20)])
print("axis ticks y:", [(e, round(Y(e), 1)) for e in (0.02, 0.04, 0.06, 0.08, 0.10, 0.12)])
