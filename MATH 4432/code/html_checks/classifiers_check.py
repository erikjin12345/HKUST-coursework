"""Numbers behind html/classifiers.html (MATH 4432 Lecture 3 / ISLP ch. 4).

Fits logistic regression, LDA, QDA, naive Bayes and KNN on the Default data
and reproduces the confusion matrices / error rates quoted in the lecture.
"""
import numpy as np, pandas as pd
import statsmodels.api as sm
from ISLP import load_data
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA, QuadraticDiscriminantAnalysis as QDA
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, roc_auc_score

D = load_data('Default')
y = (D['default'] == 'Yes').astype(int).values
D['student01'] = (D['student'] == 'Yes').astype(int)
print("n =", len(D), " defaults =", y.sum(), f"({y.mean():.2%})")

def report(name, prob, thr=0.5):
    pred = (prob >= thr).astype(int)
    cm = confusion_matrix(y, pred)          # rows: true 0/1, cols: pred 0/1
    tn, fp, fn, tp = cm.ravel()
    err = (fp + fn) / len(y)
    print(f"{name:34s} thr={thr:<4} err={err:.4f}  FP={fp:4d} FN={fn:4d}  "
          f"sens={tp/(tp+fn):.3f} spec={tn/(tn+fp):.3f}  AUC={roc_auc_score(y, prob):.3f}")

# --- logistic regression -------------------------------------------------
for cols in (['balance'], ['student01'], ['balance', 'income', 'student01']):
    X = sm.add_constant(D[cols].astype(float))
    fit = sm.GLM(y, X, family=sm.families.Binomial()).fit()
    print(f"\nlogit ~ {'+'.join(cols)}")
    print(pd.DataFrame({'coef': fit.params, 'se': fit.bse, 'z': fit.tvalues, 'p': fit.pvalues}).round(4))
    if cols == ['balance']:
        for b in (1000, 2000):
            print(f"  P(default | balance={b}) = {fit.predict([[1, b]])[0]:.4f}")
        for x in (1000, 2000):
            pass
    if cols == ['student01']:
        print(f"  P(default | student) = {fit.predict([[1,1]])[0]:.4f}, non-student = {fit.predict([[1,0]])[0]:.4f}")
    if len(cols) == 3:
        for st in (1, 0):
            print(f"  P(default | balance=1500, income=40000, student={st}) = {fit.predict([[1, 1500, 40000, st]])[0]:.4f}")
        report("logistic (balance+income+student)", fit.predict(X))

# --- LDA / QDA / NB / KNN on balance + student ----------------------------
X2 = D[['balance', 'student01']].astype(float).values
print()
lda = LDA().fit(X2, y);   report("LDA (balance+student)", lda.predict_proba(X2)[:, 1])
report("LDA (balance+student)", lda.predict_proba(X2)[:, 1], thr=0.2)
qda = QDA().fit(X2, y);   report("QDA (balance+student)", qda.predict_proba(X2)[:, 1])
nb = GaussianNB().fit(X2, y); report("Naive Bayes (balance+student)", nb.predict_proba(X2)[:, 1])
for k in (1, 5, 10):
    knn = KNeighborsClassifier(k).fit(X2, y); report(f"KNN k={k} (balance+student)", knn.predict_proba(X2)[:, 1])
print("\nnull classifier (always No): err =", round(y.mean(), 4))

# LDA sanity: priors and class means
print("\nLDA priors", lda.priors_.round(4), " means\n", pd.DataFrame(lda.means_, columns=['balance','student'], index=['No','Yes']).round(2))
