"""Numbers behind html/xbar-s2-independence.html (MATH4515 L3 part 1, Example 8, pp. 31-33).

Checks the matrix form (Xbar, Y) = M X with Y = (X_1 - Xbar, ..., X_{n-1} - Xbar),
that M is invertible, that A B^T = 0, that s^2 = g(Y), and simulates
corr(Xbar, s^2) for normal and for exponential samples.
"""
import numpy as np

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(4515)


def matrices(n):
    A = np.full((1, n), 1 / n)
    B = np.hstack([np.eye(n - 1), np.zeros((n - 1, 1))]) - 1 / n
    return A, B


# matrix form for n = 3
A, B = matrices(3)
M = np.vstack([A, B])
print("M for n = 3:\n", M)
for n in (3, 5, 10):
    A, B = matrices(n)
    M = np.vstack([A, B])
    print(f"n={n:2d}: det(M) = {np.linalg.det(M):.6f}, 1/n = {1/n:.6f}, max|A B^T| = {np.abs(A @ B.T).max():.1e}")

# with all n deviations the covariance of (Xbar, Y) is singular
n = 5
A, B_full = np.full((1, n), 1 / n), np.eye(n) - 1 / n
M_full = np.vstack([A, B_full])
print(f"all n deviations: M is {M_full.shape}, rank {np.linalg.matrix_rank(M_full)}")

# s^2 as a function of Y
x = rng.normal(size=6)
n = len(x)
Y = (x - x.mean())[:-1]
print(f"var(x, ddof=1)               = {x.var(ddof=1):.6f}")
print(f"Y'Y/(n-1)  (missing term)    = {Y @ Y / (n - 1):.6f}")
print(f"[Y'Y + (1'Y)^2]/(n-1)        = {(Y @ Y + Y.sum() ** 2) / (n - 1):.6f}")
print(f"Y'(I + 11')Y/(n-1)           = {Y @ (np.eye(n - 1) + 1) @ Y / (n - 1):.6f}")

# simulation: corr(Xbar, s^2)
reps, n = 200_000, 10
for name, draw in [("normal N(0,1)", lambda: rng.normal(size=(reps, n))),
                   ("exponential Exp(1)", lambda: rng.exponential(size=(reps, n)))]:
    X = draw()
    xbar, s2 = X.mean(axis=1), X.var(axis=1, ddof=1)
    print(f"{name:20s} corr(Xbar, s^2) = {np.corrcoef(xbar, s2)[0, 1]:+.4f}")
