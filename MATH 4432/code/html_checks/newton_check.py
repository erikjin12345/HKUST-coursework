import numpy as np, statsmodels.api as sm
from ISLP import load_data
D = load_data('Default')
y = (D['default'] == 'Yes').astype(float).values
x = D['balance'].astype(float).values
X = np.column_stack([np.ones(len(y)), x])
sig = lambda z: 1/(1+np.exp(-z))
ll = lambda b: np.sum(y*(X@b) - np.logaddexp(0, X@b))
b = np.zeros(2)
for t in range(1, 4):
    p = sig(X@b); W = p*(1-p)
    g = X.T@(y-p); H = -X.T@(X*W[:,None])
    newton = b - np.linalg.solve(H, g)
    z = X@b + (y-p)/W
    wls = sm.WLS(z, X, weights=W).fit().params
    # quadratic model value at newton point vs actual
    d = newton - b
    quad = ll(b) + g@d + 0.5*d@H@d
    print(t, "newton", newton, "wls", wls, "diff", np.max(np.abs(newton-wls)))
    print("   ll old", ll(b), "quad pred", quad, "ll new", ll(newton), "z range", z.min(), z.max())
    b = newton
