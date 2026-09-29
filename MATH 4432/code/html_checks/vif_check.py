import numpy as np, pandas as pd, statsmodels.api as sm
from ISLP import load_data
from statsmodels.stats.outliers_influence import variance_inflation_factor as VIF

C = load_data('Credit')
cols = ['Age', 'Rating', 'Limit']
P = C[cols].astype(float)
X = sm.add_constant(P)
y = C['Balance'].astype(float)
n = len(y)
full = sm.OLS(y, X).fit()
sigma2 = full.scale
print("n", n, "sigma2", sigma2, "RSE", np.sqrt(sigma2), "R2 full", full.rsquared)

Rinv = np.linalg.inv(P.corr().values)
print("corr matrix\n", P.corr().round(4))
for j, c in enumerate(cols):
    others = [k for k in cols if k != c]
    aux = sm.OLS(P[c], sm.add_constant(P[others])).fit()
    r2 = aux.rsquared
    sst = ((P[c] - P[c].mean())**2).sum()
    rss_aux = aux.ssr
    var_formula = sigma2 / (sst * (1 - r2))
    var_model = full.bse[c]**2
    print(c, "| R2_j", round(r2, 6), "| 1/(1-R2)", round(1/(1-r2), 3),
          "| statsmodels", round(VIF(X.values, j+1), 3),
          "| [Rinv]_jj", round(Rinv[j, j], 3),
          "| SE full", full.bse[c], "| SE formula", np.sqrt(var_formula),
          "| SE if R2=0", np.sqrt(sigma2/sst), "| sqrtVIF", round(np.sqrt(1/(1-r2)), 3),
          "| theta deg", round(np.degrees(np.arcsin(np.sqrt(1-r2))), 2))
