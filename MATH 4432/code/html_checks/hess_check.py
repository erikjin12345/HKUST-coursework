import numpy as np
from ISLP import load_data
D = load_data('Default')
y = (D['default'] == 'Yes').astype(float).values
x = D['balance'].astype(float).values
X = np.column_stack([np.ones(len(y)), (x - x.mean())/x.std()])
sig = lambda z: 1/(1+np.exp(-z))
grad = lambda b: X.T@(y - sig(X@b))
b = np.array([-3.0, 1.5])
p = sig(X@b); W = p*(1-p)
H = -X.T@(X*W[:,None])
h = 1e-5
Hfd = np.column_stack([(grad(b+h*e)-grad(b-h*e))/(2*h) for e in np.eye(2)])
print("analytic\n", H); print("finite diff\n", Hfd)
print("max abs diff", np.max(np.abs(H-Hfd)))
print("eigenvalues", np.linalg.eigvalsh(H))
print("sum W", W.sum(), "max W", W.max())
