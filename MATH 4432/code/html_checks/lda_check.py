import numpy as np
from scipy.stats import norm
mu = np.array([-1.0, 2.0]); pi = np.array([0.7, 0.3]); s = 1.5
for x in (0.8, 1.5):
    num = pi * norm.pdf(x, mu, s)
    p = num / num.sum()
    logterm = np.log(pi) - np.log(np.sqrt(2*np.pi)*s) - (x-mu)**2/(2*s**2)
    delta = x*mu/s**2 - mu**2/(2*s**2) + np.log(pi)
    print("x", x, "\n  num", num, "\n  p", p, "\n  log", logterm,
          "\n  delta", delta, "\n  log - delta", logterm - delta,
          "\n  const", -np.log(np.sqrt(2*np.pi)*s) - x**2/(2*s**2))
xstar = (mu[0]+mu[1])/2 + s**2*np.log(pi[0]/pi[1])/(mu[1]-mu[0])
print("boundary", xstar)
