import numpy as np
from ISLP import load_data
D = load_data('Default')
y = (D['default'] == 'Yes').astype(float).values
x = D['balance'].astype(float).values
X = np.column_stack([np.ones(len(y)), x])
sig = lambda z: 1/(1+np.exp(-z))
grad = lambda b: X.T@(y-sig(X@b))
def hess(b):
    p = sig(X@b); return -X.T@(X*(p*(1-p))[:,None])
b = np.zeros(2); path=[b.copy()]
for _ in range(25):
    b = b - np.linalg.solve(hess(b), grad(b)); path.append(b.copy())
bhat = b
print("bhat", bhat)
for t in (0, 3, 5, 7):
    bo = path[t]
    newton = bo - np.linalg.solve(hess(bo), grad(bo))
    oracle = bo - np.linalg.solve(hess(bhat), grad(bo))
    print(t, "old", bo, "\n   newton (H at old)", newton, "err", np.abs(newton-bhat),
          "\n   oracle (H at bhat)", oracle, "err", np.abs(oracle-bhat))
