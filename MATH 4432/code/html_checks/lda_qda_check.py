"""Numbers behind html/lda-qda.html: hand-computed LDA/QDA vs scikit-learn on a toy set."""
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA, QuadraticDiscriminantAnalysis as QDA
np.set_printoptions(precision=4, suppress=True)

X = np.array([[1, 2], [2, 3], [3, 3], [2, 4],           # class 1
              [5, 4], [6, 6], [7, 5], [6, 3], [6, 7]], float)  # class 2
y = np.array([1, 1, 1, 1, 2, 2, 2, 2, 2])
n, K = len(y), 2
cls = [1, 2]
pi = np.array([np.mean(y == k) for k in cls])
mu = np.array([X[y == k].mean(0) for k in cls])
S = [np.cov(X[y == k].T) for k in cls]                    # n_k - 1 in denominator
Sp = sum((np.sum(y == k) - 1) * S[i] for i, k in enumerate(cls)) / (n - K)
print("pi", pi); print("mu", mu); print("S1", S[0], "S2", S[1], sep="\n"); print("pooled", Sp, sep="\n")

x0 = np.array([3.5, 5.0])
Spi = np.linalg.inv(Sp)
for i in range(K):
    w = Spi @ mu[i]; b = -0.5 * mu[i] @ Spi @ mu[i] + np.log(pi[i])
    print(f"LDA k={i+1}: w={w}, b={b:.4f}, delta(x0)={w @ x0 + b:.4f}")
dl = np.array([Spi @ mu[i] @ x0 - 0.5 * mu[i] @ Spi @ mu[i] + np.log(pi[i]) for i in range(K)])
print("LDA softmax", np.exp(dl) / np.exp(dl).sum())
lda = LDA(store_covariance=True).fit(X, y)
print("sklearn LDA", lda.predict_proba([x0]), "cov", lda.covariance_, sep="\n")

dq = []
for i in range(K):
    Si = np.linalg.inv(S[i]); d = x0 - mu[i]
    terms = (-0.5 * x0 @ Si @ x0, x0 @ Si @ mu[i], -0.5 * mu[i] @ Si @ mu[i],
             -0.5 * np.log(np.linalg.det(S[i])), np.log(pi[i]))
    dq.append(sum(terms))
    print(f"QDA k={i+1}: terms={np.round(terms, 4)}, delta={sum(terms):.4f}, mahal={d @ Si @ d:.4f}")
dq = np.array(dq)
print("QDA softmax", np.exp(dq) / np.exp(dq).sum())
qda = QDA(store_covariance=True).fit(X, y)
print("sklearn QDA", qda.predict_proba([x0]))

# scikit-learn 1.9 uses ML divisors: n for the pooled LDA covariance, n_k for QDA
Sml = [np.cov(X[y == k].T, bias=True) for k in cls]
Spml = sum(np.sum(y == k) * Sml[i] for i, k in enumerate(cls)) / n
for name, C in (("LDA pooled/n", [Spml, Spml]), ("QDA S_k/n_k", Sml)):
    d = np.array([-0.5 * (x0 - mu[i]) @ np.linalg.inv(C[i]) @ (x0 - mu[i])
                  - 0.5 * np.log(np.linalg.det(C[i])) + np.log(pi[i]) for i in range(K)])
    print(name, np.exp(d) / np.exp(d).sum())
