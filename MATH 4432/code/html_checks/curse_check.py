"""Numbers behind html/curse.html (ISLP ch. 4, exercise 4: curse of dimensionality)."""
import numpy as np
rng = np.random.default_rng(0)

# (a) p = 1: clipped window [x-0.05, x+0.05] ∩ [0,1] vs window shifted to stay inside
clipped = 2 * ((0.05**2) / 2 + 0.05 * 0.05) + 0.9 * 0.1
print("(a) exact, clipped:", clipped, " shifted: 0.1")
X = rng.uniform(size=200_000); x0 = rng.uniform(size=2000)
print("(a) simulated, clipped:", np.mean([np.mean(np.abs(X - t) <= 0.05) for t in x0[:500]]))

# (b), (c): shifted window -> 0.1**p ; simulate p = 2, 5
for p in (1, 2, 5, 100):
    print(f"p={p:3d}: 0.1**p = {0.1**p:.3g}")
n = 1_000_000
for p in (2, 5):
    X = rng.uniform(size=(n, p)); t = rng.uniform(0.05, 0.95, size=p)
    print(f"  simulated p={p}: {np.mean(np.all(np.abs(X - t) <= 0.05, axis=1)):.3g}")

# (e) side length 0.1**(1/p)
for p in (1, 2, 3, 10, 100):
    print(f"(e) p={p:3d}: side = {0.1**(1/p):.4f}")

# (d) expected neighbours with n = 10_000 training points
for p in (1, 2, 3, 5, 10):
    print(f"(d) p={p:2d}: expected points in box with n=10000: {10_000 * 0.1**p:g}")
