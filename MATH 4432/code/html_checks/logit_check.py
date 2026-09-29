import numpy as np, statsmodels.api as sm
from ISLP import load_data

D = load_data('Default')
y = (D['default'] == 'Yes').astype(float).values
x = D['balance'].astype(float).values
n = len(y)
X = np.column_stack([np.ones(n), x])
sig = lambda z: 1/(1+np.exp(-z))
ll = lambda b: np.sum(y*(X@b) - np.logaddexp(0, X@b))
print("n", n, "defaults", int(y.sum()))

# Newton-Raphson / IRLS
b = np.zeros(2)
for it in range(1, 30):
    p = sig(X@b); W = p*(1-p)
    g = X.T@(y-p); H = X.T@(X*W[:,None])
    step = np.linalg.solve(H, g); b = b + step
    print("newton", it, b, round(ll(b), 4))
    if np.max(np.abs(step)) < 1e-10: break
p = sig(X@b); W = p*(1-p)
se = np.sqrt(np.diag(np.linalg.inv(X.T@(X*W[:,None]))))
print("SE", se, "z", b/se)

# Gradient ascent on standardized x
mu, sd = x.mean(), x.std()
Z = np.column_stack([np.ones(n), (x-mu)/sd])
g_ = np.zeros(2); alpha = 1.0
for it in range(1, 200001):
    p_ = sig(Z@g_); grad = Z.T@(y-p_)/n
    g_ = g_ + alpha*grad
    if np.max(np.abs(grad)) < 1e-9: break
b1 = g_[1]/sd; b0 = g_[0] - g_[1]*mu/sd
print("GD iters", it, "b0", b0, "b1", b1)

m = sm.Logit(y, X).fit(disp=0)
print("statsmodels", m.params, m.bse, "llf", m.llf)
for v in (1000, 2000):
    print("p(balance=%d)" % v, sig(b[0]+b[1]*v))
print("grad at optimum", X.T@(y-sig(X@b)))
print("sum p_hat", sig(X@b).sum(), "sum y", y.sum())
print("boundary balance p=0.5", -b[0]/b[1])
