"""Numbers behind html/importance.html (MATH4515 L2, Example 10).

Prices a deep out-of-the-money European call with plain Monte Carlo and with
importance sampling on W_T, and compares a few choices of proposal g.
"""
import numpy as np
from scipy.stats import norm

S0, X, sigma, r, T = 100.0, 250.0, 0.2, 0.03, 1.0
n = 1_000_000
rng = np.random.default_rng(4515)

# Black–Scholes reference
d1 = (np.log(S0 / X) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
bs = S0 * norm.cdf(d1) - X * np.exp(-r * T) * norm.cdf(d2)
p_itm = norm.cdf(d2)  # P_Q(S_T > X)
mu = (np.log(X / S0) - (r - sigma**2 / 2) * T) / sigma


def payoff_from_w(w):
    ST = S0 * np.exp((r - sigma**2 / 2) * T + sigma * w)
    return np.exp(-r * T) * np.maximum(ST - X, 0.0), ST


def report(name, V, hits):
    est, se = V.mean(), V.std(ddof=1) / np.sqrt(n)
    print(f"{name:34s} est={est:.4e}  SE={se:.2e}  PE={se/est*100:6.3f}%  hits={hits}")


print(f"BS price = {bs:.6e}   P_Q(S_T > X) = {p_itm:.4e} = {p_itm*100:.6f}%   mu = {mu:.4f}")

# 1. plain Monte Carlo: W_T ~ N(0, T)
w = rng.normal(0, np.sqrt(T), n)
V, ST = payoff_from_w(w)
report("plain MC", V, int((ST > X).sum()))

# 2. importance sampling, shifted normal N(mu, T); f/g = exp(-mu w/T + mu^2/(2T))
def is_shift(m):
    w = rng.normal(m, np.sqrt(T), n)
    V, ST = payoff_from_w(w)
    lr = np.exp(-m * w / T + m**2 / (2 * T))
    return V * lr, int((ST > X).sum())

for m in [mu / 2, mu, mu + 1, mu + 3]:
    V, hits = is_shift(m)
    report(f"IS shift mu={m:.3f}", V, hits)

# 3. importance sampling with a truncated normal on [mu, inf): g = f(w)/P_f(W>mu) for w>mu
#    f/g = P_f(W > mu) = 1 - Phi(mu/sqrt(T)), a constant
tail = 1 - norm.cdf(mu / np.sqrt(T))
u = rng.uniform(norm.cdf(mu / np.sqrt(T)), 1.0, n)
w = norm.ppf(u) * np.sqrt(T)
V, ST = payoff_from_w(w)
report("IS truncated normal on [mu, inf)", V * tail, int((ST > X).sum()))

# 4. wrong direction: a put priced with the right-shifted g
def put_from_w(w):
    ST = S0 * np.exp((r - sigma**2 / 2) * T + sigma * w)
    return np.exp(-r * T) * np.maximum(X - ST, 0.0)

bs_put = X * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
w = rng.normal(mu, np.sqrt(T), n)
Vp = put_from_w(w) * np.exp(-mu * w / T + mu**2 / (2 * T))
w0 = rng.normal(0, np.sqrt(T), n)
Vp0 = put_from_w(w0)
print(f"\nput: BS={bs_put:.4f}  plain est={Vp0.mean():.4f} SE={Vp0.std(ddof=1)/np.sqrt(n):.2e}"
      f"  | right-shifted IS est={Vp.mean():.4f} SE={Vp.std(ddof=1)/np.sqrt(n):.2e}")
