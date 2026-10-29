"""Numbers behind html/integration-order.html (MATH4515 L3 part 1, example (b)).

X, Y i.i.d. Exp(1), joint density e^{-(x+y)} on x, y >= 0.
P(X <= Y <= 3) computed in both integration orders, in closed form and numerically.
"""
import numpy as np
from scipy.integrate import dblquad

f = lambda y, x: np.exp(-(x + y))  # dblquad integrates the first argument innermost

# dy innermost: x in [0, 3], y in [x, 3]
num_dydx, _ = dblquad(f, 0, 3, lambda x: x, lambda x: 3)
# dx innermost: y in [0, 3], x in [0, y]
num_dxdy, _ = dblquad(lambda x, y: np.exp(-(x + y)), 0, 3, lambda y: 0, lambda y: y)

closed = 0.5 - np.exp(-3) + 0.5 * np.exp(-6)
wrong = 0.5 * np.exp(-6) - 0.5  # from dropping the upper term and the sign at y = x

print(f"closed form 1/2 - e^-3 + e^-6/2 = {closed:.6f}")
print(f"numeric, dy innermost           = {num_dydx:.6f}")
print(f"numeric, dx innermost           = {num_dxdy:.6f}")
print(f"wrong answer e^-6/2 - 1/2       = {wrong:.6f}")

# inner integral at a few x, closed form vs numeric
from scipy.integrate import quad
for x in (0.0, 1.0, 2.0, 2.9):
    inner = np.exp(-2 * x) - np.exp(-x - 3)
    q, _ = quad(lambda y: np.exp(-(x + y)), x, 3)
    print(f"x={x:3.1f}: e^-2x - e^-(x+3) = {inner:.6f}, quad = {q:.6f}")

# Monte Carlo sanity check
rng = np.random.default_rng(4515)
X, Y = rng.exponential(size=(2, 2_000_000))
print(f"Monte Carlo                     = {np.mean((X <= Y) & (Y <= 3)):.6f}")
