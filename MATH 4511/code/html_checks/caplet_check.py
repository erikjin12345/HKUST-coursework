"""Numbers behind html/caplet.html (MATH4511 L2, Example 20, s. 109-112).

Replicates a caplet and a floorlet with the market bond options on a 2-year
zero coupon bond (face 100), and checks the scaling argument numerically.
"""
import numpy as np

# Market options on a 2-year ZCB with face value 100: (type, maturity, strike, price)
options = {
    "A": ("call", 1.0, 95, 2.8),   "B": ("call", 1.0, 98, 1.3),
    "C": ("call", 1.5, 95, 5.2),   "D": ("call", 1.5, 98, 2.9),
    "E": ("put", 1.0, 95, 3.43),   "F": ("put", 1.0, 98, 4.788),
    "G": ("put", 1.5, 95, 3.4),    "H": ("put", 1.5, 98, 3.88),
}

# (a) caplet on R[1,2], K = 5.263 % annual effective, N = 5000, paid at T2 = 2
N, K = 5000, 0.05263
lam = N * (1 + K) / 100
print(f"(a) face N(1+K) = {N*(1+K):.2f}, strike N = {N}")
print(f"    lambda = {lam:.4f}, scaled strike = {N/lam:.4f} = 100/(1+K) = {100/(1+K):.4f}")
print(f"    price = {lam:.4f} x {options['E'][3]} = {lam*options['E'][3]:.3f}")

# payoff check over a grid of future rates R[1,2]: caplet value at t=1 vs lam puts
R = np.linspace(0.0, 0.15, 301)
caplet_t1 = N * np.maximum(R - K, 0) / (1 + R)
puts_t1 = lam * np.maximum(100 / (1 + K) - 100 / (1 + R), 0)
print(f"    max |caplet - lam*put| on R in [0, 15%] = {np.abs(caplet_t1 - puts_t1).max():.2e}")

# Which caplet strike rate does each 1-year put replicate?
print("\nStrike ratio and implied caplet rate for the 1-year puts:")
for name in ["E", "F"]:
    _, T, X, P = options[name]
    K_impl = 100 / X - 1
    lam_impl = N * (1 + K_impl) / 100
    print(f"    {name}: X/100 = {X/100:.2f}  ->  K = {K_impl*100:.4f} %,"
          f"  caplet (N={N}) = {lam_impl:.4f} x {P} = {lam_impl*P:.3f}")

# What if F were used with the 5.263 % caplet's scaling? Payoff mismatch
wrong = lam * np.maximum(98 - 100 / (1 + R), 0)
i = np.argmin(np.abs(R - 0.04))
print(f"\n    R = 4 %: caplet pays {caplet_t1[i]:.2f} at t=1, lam x F pays {wrong[i]:.2f}")

# (b) floorlet on R[1.5,2], K = 4.1216 % annual effective -> half-year rate, N = 10000
N, K_eff = 10000, 0.041216
K = (1 + K_eff) ** 0.5 - 1
lam = N * (1 + K) / 100
print(f"\n(b) K[1.5,2] = {K*100:.4f} % per half year, lambda = {lam:.4f},"
      f" scaled strike = {N/lam:.4f}")
print(f"    price = {lam:.4f} x {options['D'][3]} = {lam*options['D'][3]:.3f}")
R = np.linspace(0.0, 0.08, 301)
floor_t15 = N * np.maximum(K - R, 0) / (1 + R)
calls = lam * np.maximum(100 / (1 + R) - 100 / (1 + K), 0)
print(f"    max |floorlet - lam*call| on R in [0, 8%] = {np.abs(floor_t15 - calls).max():.2e}")
