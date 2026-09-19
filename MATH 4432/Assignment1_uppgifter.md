# MATH 4432 – Assignment 1

**Datum:** 17 september 2026
**Deadline:** 30 september 2026, 23:59 (Canvas)

## Inlämning

Två filer krävs:

1. En `.pdf` med alla teoretiska delar (fotograferad handskrift går bra).
2. En `.html` eller `.pdf` som genererats automatiskt från en `.ipynb`/`.Rmd` med all kod och alla resultat. **0 poäng på koddelen om formatet inte följs.**

Rå `.ipynb`/`.Rmd` är frivillig.

Bok: *An Introduction to Statistical Learning*, 2:a upplagan (https://www.statlearning.com/). Texten nedan är hämtad från Python-versionen (ISLP), som har samma uppgiftsnummer. Datasetten laddas med `from ISLP import load_data`.

| Uppgift | Typ | Var |
|---|---|---|
| Kap. 2: 1, 3 | teori | PDF |
| Kap. 2: 8, 10 | kod | notebook |
| Kap. 3: 1, 5 | teori | PDF |
| Kap. 3: 8, 9 | kod | notebook |
| Bias-variance | kod | notebook |

---

## Kapitel 2

### Uppgift 1 (teori)

For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

- (a) The sample size n is extremely large, and the number of predictors p is small.
- (b) The number of predictors p is extremely large, and the number of observations n is small.
- (c) The relationship between the predictors and response is highly non-linear.
- (d) The variance of the error terms, i.e. σ² = Var(ε), is extremely high.

### Uppgift 3 (teori)

We now revisit the bias-variance decomposition.

- (a) Provide a sketch of typical (squared) bias, variance, training error, test error, and Bayes (or irreducible) error curves, on a single plot, as we go from less flexible statistical learning methods towards more flexible approaches. The x-axis should represent the amount of flexibility in the method, and the y-axis should represent the values for each curve. There should be five curves. Make sure to label each one.
- (b) Explain why each of the five curves has the shape displayed in part (a).

### Uppgift 8 (kod) – `College`

This exercise relates to the `College` data set. It contains a number of variables for 777 different universities and colleges in the US. The variables are

- `Private`: Public/private indicator
- `Apps`: Number of applications received
- `Accept`: Number of applicants accepted
- `Enroll`: Number of new students enrolled
- `Top10perc`: New students from top 10 % of high school class
- `Top25perc`: New students from top 25 % of high school class
- `F.Undergrad`: Number of full-time undergraduates
- `P.Undergrad`: Number of part-time undergraduates
- `Outstate`: Out-of-state tuition
- `Room.Board`: Room and board costs
- `Books`: Estimated book costs
- `Personal`: Estimated personal spending
- `PhD`: Percent of faculty with Ph.D.s
- `Terminal`: Percent of faculty with terminal degree
- `S.F.Ratio`: Student/faculty ratio
- `perc.alumni`: Percent of alumni who donate
- `Expend`: Instructional expenditure per student
- `Grad.Rate`: Graduation rate

- (a) Use the `pd.read_csv()` function to read the data into Python. Call the loaded data `college`. *(Alternativ: `college = load_data('College')`.)*
- (b) Look at the data. The first column is just the name of each university. Set it as the index so that the first data column is `Private`:
  ```python
  college2 = pd.read_csv('College.csv', index_col=0)
  college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
  college3 = college3.set_index('College')
  college = college3
  ```
- (c) Use the `describe()` method to produce a numerical summary of the variables in the data set.
- (d) Use the `pd.plotting.scatter_matrix()` function to produce a scatterplot matrix of the first columns `[Top10perc, Apps, Enroll]`.
- (e) Use the `boxplot()` method of `college` to produce side-by-side boxplots of `Outstate` versus `Private`.
- (f) Create a new qualitative variable, called `Elite`, by binning the `Top10perc` variable into two groups based on whether or not the proportion of students coming from the top 10 % of their high school classes exceeds 50 %.
  ```python
  college['Elite'] = pd.cut(college['Top10perc'], [0, 0.5, 1], labels=['No', 'Yes'])
  ```
  Use the `value_counts()` method of `college['Elite']` to see how many elite universities there are. Finally, use the `boxplot()` method again to produce side-by-side boxplots of `Outstate` versus `Elite`.
- (g) Use the `plot.hist()` method of `college` to produce some histograms with differing numbers of bins for a few of the quantitative variables. The command `plt.subplots(2, 2)` may be useful.
- (h) Continue exploring the data, and provide a brief summary of what you discover.

### Uppgift 10 (kod) – `Boston`

This exercise involves the `Boston` housing data set.

- (a) To begin, load in the `Boston` data set, which is part of the ISLP library.
- (b) How many rows are in this data set? How many columns? What do the rows and columns represent?
- (c) Make some pairwise scatterplots of the predictors (columns) in this data set. Describe your findings.
- (d) Are any of the predictors associated with per capita crime rate? If so, explain the relationship.
- (e) Do any of the suburbs of Boston appear to have particularly high crime rates? Tax rates? Pupil-teacher ratios? Comment on the range of each predictor.
- (f) How many of the suburbs in this data set bound the Charles river?
- (g) What is the median pupil-teacher ratio among the towns in this data set?
- (h) Which suburb of Boston has lowest median value of owner-occupied homes? What are the values of the other predictors for that suburb, and how do those values compare to the overall ranges for those predictors? Comment on your findings.
- (i) In this data set, how many of the suburbs average more than seven rooms per dwelling? More than eight rooms per dwelling? Comment on the suburbs that average more than eight rooms per dwelling.

---

## Kapitel 3

### Uppgift 1 (teori)

Describe the null hypotheses to which the p-values given in Table 3.4 correspond. Explain what conclusions you can draw based on these p-values. Your explanation should be phrased in terms of `sales`, `TV`, `radio`, and `newspaper`, rather than in terms of the coefficients of the linear model.

**Table 3.4** (Advertising data, multiple linear regression of units sold on TV, radio and newspaper budgets):

| | Coefficient | Std. error | t-statistic | p-value |
|---|---|---|---|---|
| Intercept | 2.939 | 0.3119 | 9.42 | < 0.0001 |
| TV | 0.046 | 0.0014 | 32.81 | < 0.0001 |
| radio | 0.189 | 0.0086 | 21.89 | < 0.0001 |
| newspaper | −0.001 | 0.0059 | −0.18 | 0.8599 |

### Uppgift 5 (teori)

Consider the fitted values that result from performing linear regression without an intercept. In this setting, the i-th fitted value takes the form

$$\hat y_i = x_i \hat\beta, \qquad \text{where} \qquad \hat\beta = \frac{\sum_{i=1}^n x_i y_i}{\sum_{i'=1}^n x_{i'}^2}. \tag{3.38}$$

Show that we can write

$$\hat y_i = \sum_{i'=1}^n a_{i'} y_{i'}.$$

What is $a_{i'}$?

### Uppgift 8 (kod) – enkel linjär regression på `Auto`

This question involves the use of simple linear regression on the `Auto` data set.

- (a) Use the `sm.OLS()` function to perform a simple linear regression with `mpg` as the response and `horsepower` as the predictor. Use the `summarize()` function to print the results. Comment on the output. For example:
  - i. Is there a relationship between the predictor and the response?
  - ii. How strong is the relationship between the predictor and the response?
  - iii. Is the relationship between the predictor and the response positive or negative?
  - iv. What is the predicted `mpg` associated with a `horsepower` of 98? What are the associated 95 % confidence and prediction intervals?
- (b) Plot the response and the predictor in a new set of axes `ax`. Use the `ax.axline()` method or the `abline()` function defined in the lab to display the least squares regression line.
- (c) Produce some diagnostic plots of the least squares regression fit as described in the lab. Comment on any problems you see with the fit.

### Uppgift 9 (kod) – multipel linjär regression på `Auto`

This question involves the use of multiple linear regression on the `Auto` data set.

- (a) Produce a scatterplot matrix which includes all of the variables in the data set.
- (b) Compute the matrix of correlations between the variables using the `DataFrame.corr()` method.
- (c) Use the `sm.OLS()` function to perform a multiple linear regression with `mpg` as the response and all other variables except `name` as the predictors. Use the `summarize()` function to print the results. Comment on the output. For instance:
  - i. Is there a relationship between the predictors and the response? Use the `anova_lm()` function from statsmodels to answer this question.
  - ii. Which predictors appear to have a statistically significant relationship to the response?
  - iii. What does the coefficient for the `year` variable suggest?
- (d) Produce some diagnostic plots of the linear regression fit as described in the lab. Comment on any problems you see with the fit. Do the residual plots suggest any unusually large outliers? Does the leverage plot identify any observations with unusually high leverage?
- (e) Fit some models with interactions as described in the lab. Do any interactions appear to be statistically significant?
- (f) Try a few different transformations of the variables, such as log(X), √X, X². Comment on your findings.

---

## Extra kodningsuppgift: bias-variance trade-off

Consider the ground truth model

$$y = \sin(2 x_1).$$

Generate $n_{\text{train}} = 50$ training samples with random noise $\mathcal{N}(0, 0.5^2)$ and test data with sample size $n_{\text{test}} = 500$.

Suppose there are $p$ predictors $\{x_i\}_{i=1}^p$, where $\{x_j : j \neq 1\}$ is a set of noisy predictors that are unrelated to $y$.

Apply linear regression and KNN regression to predict $y$ in the test set and analyze the bias-variance trade-off for both models.

Vary $p \in \{1, 2, 3, 4, 10, 20\}$ and $k = 1, \ldots, 9$ for KNN.

Visualize the patterns of bias-variance trade-off. For your reference, the pattern of mean square error should be similar to FIGURE 3.20 (page 115) in the reference book.

### Kodmall från uppgiften (luckor markerade `DO`)

```python
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression

ntrain = 50            # Training
ntest = 500            # Test
nrep = 100             # Repeat 100 times
p = 20
puse = np.array([1, 2, 3, 4, 10, 20])   # Number of predictors
k = np.arange(1, 10)
sigma = 0.5

Xtrain = np.random.uniform(-1, 1, [ntrain, p])
Xtest = np.random.uniform(-1, 1, [ntest, p])
y0 = np.sin(2 * Xtrain[:, 0])          # Only the first predictor is related to y
ytest = np.sin(2 * Xtest[:, 0])

out_knn = pd.DataFrame()               # Output results
out_lm = pd.DataFrame()

for i in range(len(puse)):
    yhat_lm = np.zeros((ntest, nrep))
    yhat_knn = np.zeros((ntest, nrep, len(k)))
    for l in range(nrep):
        y = y0 + np.random.normal(0, sigma, ntrain)

        ######### DO: fit linear regression using LinearRegression function, assign predicted value to yhat_lm[:, [l]] #########
        fit_lm =
        yhat_lm[:, l] =                # Predicted value

        for j in range(len(k)):
            ######### DO: fit knn using KNeighborsRegressor function, assign predicted value to yhat_knn[:, l, j] #########
            fit_knn =
            yhat_knn[:, l, j] =        # Predicted value

        print(i + 1, "-th p, ", l + 1, "-th repetition finished. \n")

    ######### DO: compute bias and variance of linear regression #########
    ybar_lm =                          # E(f^hat)
    biasSQ_lm =                        # E[ (f - E(f^hat))^2 ]
    variance_lm =                      # E[ (E(f^hat) - f^hat)^2 ]
    err_lm =                           # total MSE
    out_lm = pd.concat([out_lm, pd.DataFrame({'biasSQ_lm': [biasSQ_lm], 'variance_lm': [variance_lm],
                                              'MSE': [err_lm], 'p': [puse[i]]})])

    ######### DO: compute bias and variance of knn regression #########
    for j in range(len(k)):
        ybar_knn =                     # E(f^hat)
        biasSQ_knn =                   # E[ (f - E(f^hat))^2 ]
        variance_knn =                 # E[ (E(f^hat) - f^hat)^2 ]
        err_knn =                      # total MSE
        out_knn = pd.concat([out_knn, pd.DataFrame({'biasSQ_knn': [biasSQ_knn], 'variance_knn': [variance_knn],
                                                    'MSE': [err_knn], '1/K': [1 / k[j]], 'p': [puse[i]]})])
```
