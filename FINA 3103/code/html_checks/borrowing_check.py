"""Numbers behind html/borrowing.html (FINA 3103 Assignment 1, Part B (c)).

Lending earns rf = 3 %, borrowing costs r_borrow = 6 %. Computes
1) the kinked CAL with the risky portfolio fixed at P* (the textbook model),
2) the full problem where the investor may also change the stock-bond mix,
   checked against a brute-force numerical optimisation,
and prints the SVG coordinates for the figure.
"""
import numpy as np
from scipy.optimize import minimize

E = np.array([0.10, 0.06])
s_S, s_B, rho = 0.18, 0.10, 0.25
rf, rb = 0.03, 0.06
Sigma = np.array([[s_S**2, rho * s_S * s_B], [rho * s_S * s_B, s_B**2]])
members = {"elaine": 3.0, "chen": 1.5}

def tangency(r):
    z = np.linalg.solve(Sigma, E - r)
    w = z / z.sum()
    return w, w @ E, np.sqrt(w @ Sigma @ w)

wP, EP, sP = tangency(rf)
wPB, EPB, sPB = tangency(rb)
print(f"P*  (tangent from rf={rf:.0%}): w = {wP.round(4)}, E = {EP:.4f}, sigma = {sP:.4f}, "
      f"Sharpe vs rf = {(EP-rf)/sP:.4f}, slope beyond P* vs rb = {(EP-rb)/sP:.4f}")
print(f"P_B (tangent from rb={rb:.0%}): w = {wPB.round(4)}, E = {EPB:.4f}, sigma = {sPB:.4f}, "
      f"Sharpe vs rb = {(EPB-rb)/sPB:.4f}")

# 1) kinked CAL with P* fixed
print("\n1) P* fixed")
A_lo, A_hi = (EP - rb) / sP**2, (EP - rf) / sP**2
print(f"   y* = 1 for {A_lo:.4f} <= A <= {A_hi:.4f}")
for name, A in members.items():
    yL, yB = (EP - rf) / (A * sP**2), (EP - rb) / (A * sP**2)
    y, r = (yL, rf) if yL <= 1 else ((yB, rb) if yB >= 1 else (1.0, rf))
    U_old = rf + yL * (EP - rf) - 0.5 * A * yL**2 * sP**2
    U = r + y * (EP - r) - 0.5 * A * y**2 * sP**2
    print(f"   {name}: yL={yL:.4f} yB={yB:.4f} -> y*={y:.4f}, w=(S {y*wP[0]:.4f}, B {y*wP[1]:.4f}, "
          f"rf {1-y:.4f}), E_C={r + y*(EP-r):.4f}, U old={U_old:.4f} new={U:.4f}")

# 2) mix free: closed form on the frontier segment (100 % risky)
print("\n2) mix free")
d = Sigma[0, 0] + Sigma[1, 1] - 2 * Sigma[0, 1]
A2_lo, A2_hi = (EPB - rb) / sPB**2, A_hi
print(f"   100 % risky (on the curve between P* and P_B) for {A2_lo:.4f} <= A <= {A2_hi:.4f}")
def U_full(x, A):
    xs, xb = x
    rate = rf if 1 - xs - xb >= 0 else rb
    ret = xs * E[0] + xb * E[1] + (1 - xs - xb) * rate
    return ret - 0.5 * A * (np.array(x) @ Sigma @ np.array(x))
for name, A in members.items():
    w = ((E[0] - E[1]) / A + Sigma[1, 1] - Sigma[0, 1]) / d
    x = np.array([w, 1 - w])
    Ec, sc = x @ E, np.sqrt(x @ Sigma @ x)
    best = max((minimize(lambda v: -U_full(v, A), x0, method="Nelder-Mead",
                         options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 20000})
                for x0 in ([0.5, 0.5], [1.5, 0.0], [0.3, 0.3], [2.0, -0.5])), key=lambda r: -r.fun)
    print(f"   {name}: w_S={w:.4f}, w_B={1-w:.4f}, E={Ec:.4f}, sigma={sc:.4f}, U={U_full(x, A):.4f} | "
          f"numerical: x={best.x.round(4)}, U={-best.fun:.4f}")

# SVG coordinates: sigma 0..0.36 -> x 60..680, E 0.02..0.14 -> y 320..20
X = lambda s: 60 + s / 0.36 * 620
Y = lambda e: 320 - (e - 0.02) / 0.12 * 300
pts = []
for w in np.linspace(-0.2, 2.0, 45):
    x = np.array([w, 1 - w])
    pts.append(f"{X(np.sqrt(x @ Sigma @ x)):.1f},{Y(x @ E):.1f}")
print("\nfrontier path: M" + " L".join(pts))
for name, s, e in [("rf", 0, rf), ("rb", 0, rb), ("S", s_S, E[0]), ("B", s_B, E[1]),
                   ("P*", sP, EP), ("P_B", sPB, EPB)]:
    print(f"{name}: ({X(s):.1f}, {Y(e):.1f})")
print(f"kinked beyond P* to sigma=0.36: ({X(0.36):.1f}, {Y(rb + (EP-rb)/sP*0.36):.1f})")
print(f"rb line to sigma=0.36: ({X(0.36):.1f}, {Y(rb + (EPB-rb)/sPB*0.36):.1f})")
print("ticks x:", [(s, round(X(s), 1)) for s in (0, 0.1, 0.2, 0.3)])
print("ticks y:", [(e, round(Y(e), 1)) for e in (0.02, 0.06, 0.10, 0.14)])
