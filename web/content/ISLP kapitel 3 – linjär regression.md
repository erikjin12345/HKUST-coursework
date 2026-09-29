# ISLP kapitel 3 – Linjär regression

Formlerna nedan följer *An Introduction to Statistical Learning with Applications in Python*, kapitel 3. Numrering "(3.x)" är bokens. Sidhänvisningar avser `HKUST books/ISLP_website (1).pdf`.

## 3.1 Enkel linjär regression (s. 69–82)

Modell och skattning:

$$
Y \approx \beta_0 + \beta_1 X, \qquad \hat y_i = \hat\beta_0 + \hat\beta_1 x_i, \qquad e_i = y_i - \hat y_i \tag{3.1–3.3}
$$

Minsta kvadrat minimerar residualkvadratsumman

$$
\mathrm{RSS} = \sum_{i=1}^{n} e_i^2 = \sum_{i=1}^{n}\big(y_i - \hat\beta_0 - \hat\beta_1 x_i\big)^2
$$

med lösningen

$$
\hat\beta_1 = \frac{\sum_{i=1}^{n}(x_i - \bar x)(y_i - \bar y)}{\sum_{i=1}^{n}(x_i - \bar x)^2}, \qquad
\hat\beta_0 = \bar y - \hat\beta_1 \bar x \tag{3.4}
$$

### Osäkerhet i skattningarna (s. 73–77)

Med sann modell $Y = \beta_0 + \beta_1 X + \varepsilon$, $\mathrm{Var}(\varepsilon) = \sigma^2$:

$$
\mathrm{SE}(\hat\beta_0)^2 = \sigma^2\left[\frac{1}{n} + \frac{\bar x^2}{\sum_{i}(x_i - \bar x)^2}\right], \qquad
\mathrm{SE}(\hat\beta_1)^2 = \frac{\sigma^2}{\sum_{i}(x_i - \bar x)^2} \tag{3.8}
$$

$\sigma$ skattas med **residual standard error**

$$
\mathrm{RSE} = \sqrt{\frac{\mathrm{RSS}}{n - 2}}
$$

Ungefärligt 95 % konfidensintervall:

$$
\hat\beta_1 \pm 2\,\mathrm{SE}(\hat\beta_1) \tag{3.9}
$$

Hypotestest $H_0: \beta_1 = 0$ mot $H_a: \beta_1 \neq 0$ med

$$
t = \frac{\hat\beta_1 - 0}{\mathrm{SE}(\hat\beta_1)} \sim t_{n-2} \text{ under } H_0 \tag{3.14}
$$

### Modellens kvalitet (s. 77–80)

$$
\mathrm{TSS} = \sum_{i}(y_i - \bar y)^2, \qquad
R^2 = \frac{\mathrm{TSS} - \mathrm{RSS}}{\mathrm{TSS}} = 1 - \frac{\mathrm{RSS}}{\mathrm{TSS}} \tag{3.17}
$$

I enkel regression gäller $R^2 = \mathrm{Cor}(X, Y)^2$, där

$$
\mathrm{Cor}(X, Y) = \frac{\sum_i (x_i - \bar x)(y_i - \bar y)}{\sqrt{\sum_i (x_i - \bar x)^2}\,\sqrt{\sum_i (y_i - \bar y)^2}} \tag{3.18}
$$

### Konfidens- och prediktionsintervall vid $x_0$ (Auto-uppgift 8)

$$
\hat y_0 \pm t_{n-2,\,\alpha/2}\; \mathrm{RSE}\,\sqrt{\frac{1}{n} + \frac{(x_0 - \bar x)^2}{\sum_i (x_i - \bar x)^2}}
\qquad\text{(konfidens för } \mathbb{E}[Y \mid x_0])
$$

$$
\hat y_0 \pm t_{n-2,\,\alpha/2}\; \mathrm{RSE}\,\sqrt{1 + \frac{1}{n} + \frac{(x_0 - \bar x)^2}{\sum_i (x_i - \bar x)^2}}
\qquad\text{(prediktion för en ny observation)}
$$

## 3.2 Multipel linjär regression (s. 82–92)

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \varepsilon \tag{3.19}
$$

$$
\mathrm{RSS} = \sum_{i=1}^{n}\big(y_i - \hat\beta_0 - \hat\beta_1 x_{i1} - \dots - \hat\beta_p x_{ip}\big)^2 \tag{3.22}
$$

I matrisform, med $\mathbf X$ av storlek $n \times (p+1)$ inklusive en kolumn ettor:

$$
\hat{\boldsymbol\beta} = (\mathbf X^{\top}\mathbf X)^{-1}\mathbf X^{\top}\mathbf y, \qquad
\hat{\mathbf y} = \mathbf X\hat{\boldsymbol\beta} = \mathbf H\mathbf y, \qquad
\mathbf H = \mathbf X(\mathbf X^{\top}\mathbf X)^{-1}\mathbf X^{\top}
$$

### Finns något samband alls? F-testet (s. 84–87)

$$
H_0: \beta_1 = \beta_2 = \dots = \beta_p = 0 \quad\text{mot}\quad H_a: \text{minst ett } \beta_j \neq 0
$$

$$
F = \frac{(\mathrm{TSS} - \mathrm{RSS})/p}{\mathrm{RSS}/(n - p - 1)} \sim F_{p,\;n-p-1} \text{ under } H_0 \tag{3.23}
$$

Under antagandena gäller $\mathbb{E}\{\mathrm{RSS}/(n-p-1)\} = \sigma^2$ alltid, och $\mathbb{E}\{(\mathrm{TSS}-\mathrm{RSS})/p\} = \sigma^2$ när $H_0$ är sann, så $F \approx 1$ under $H_0$ och $F \gg 1$ annars.

Test av en delmängd med $q$ koefficienter, där $\mathrm{RSS}_0$ är residualsumman för modellen utan dem:

$$
F = \frac{(\mathrm{RSS}_0 - \mathrm{RSS})/q}{\mathrm{RSS}/(n - p - 1)} \tag{3.24}
$$

För $q = 1$ är $F = t^2$ för den koefficienten. Detta är vad `anova_lm` räknar.

### Kvalitetsmått (s. 88–90)

$$
\mathrm{RSE} = \sqrt{\frac{\mathrm{RSS}}{n - p - 1}}, \qquad
R^2 = \mathrm{Cor}(Y, \hat Y)^2 \tag{3.25}
$$

$R^2$ ökar alltid när en variabel läggs till, även en meningslös. Justerat $R^2$ straffar antalet variabler:

$$
R^2_{\text{adj}} = 1 - \frac{\mathrm{RSS}/(n - p - 1)}{\mathrm{TSS}/(n - 1)}
$$

### Variabelselektion (s. 87–88)

Antal delmängder är $2^p$. Stegvisa metoder: **forward** lägger till den variabel som sänker RSS mest, **backward** tar bort den med högst p-värde, **mixed** gör båda och tar bort variabler vars p-värde stiger över en gräns när nya kommer in.

## 3.3 Andra frågor (s. 92–118)

### Kvalitativa prediktorer (s. 92–96)

Två nivåer, dummyvariabel:

$$
x_i = \begin{cases} 1 & \text{om nivå A} \\ 0 & \text{annars} \end{cases}
\qquad
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i =
\begin{cases} \beta_0 + \beta_1 + \varepsilon_i & \text{nivå A} \\ \beta_0 + \varepsilon_i & \text{referens} \end{cases} \tag{3.27}
$$

$\beta_0$ är referensnivåns medelvärde och $\beta_1$ skillnaden mot den. En variabel med $k$ nivåer kodas med $k - 1$ dummies. I statsmodels: `C(origin)`.

### Interaktion (s. 96–100)

$$
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 X_1 X_2 + \varepsilon
= \beta_0 + (\beta_1 + \beta_3 X_2)\,X_1 + \beta_2 X_2 + \varepsilon \tag{3.31–3.32}
$$

Effekten av $X_1$ beror på nivån av $X_2$. **Hierarkiprincipen:** om interaktionen $X_1 X_2$ är med ska även huvudeffekterna $X_1$ och $X_2$ vara med, oavsett deras p-värden.

### Polynomregression (s. 100–101)

$$
\mathrm{mpg} = \beta_0 + \beta_1\,\mathrm{horsepower} + \beta_2\,\mathrm{horsepower}^2 + \varepsilon \tag{3.36}
$$

Fortfarande en linjär modell i koefficienterna, så minsta kvadrat fungerar oförändrat.

### Diagnostik (s. 101–113)

| Problem | Symptom | Åtgärd |
|---|---|---|
| Icke-linjäritet | Mönster i residualer mot $\hat y$ | Transformera $X$: $\log X$, $\sqrt X$, $X^2$ |
| Korrelerade fel | Residualer följer varandra över index eller tid | Tidsseriemetoder; SE underskattas annars |
| Heteroskedasticitet | Trattform i residualplotten | Transformera $Y$: $\log Y$, $\sqrt Y$; viktad regression |
| Outliers | Studentiserad residual $\lvert e_i / \hat\sigma_{(i)} \rvert > 3$ | Kontrollera datan; rapportera med och utan |
| Hög hävstång | $h_i$ långt över medel $(p+1)/n$ | Undersök; punkten styr anpassningen |
| Kollinearitet | Stora SE, instabila tecken, hög VIF | Ta bort eller kombinera variabler |

Hävstång i enkel regression:

$$
h_i = \frac{1}{n} + \frac{(x_i - \bar x)^2}{\sum_{i'}(x_{i'} - \bar x)^2}, \qquad \frac{1}{n} \le h_i \le 1, \qquad \bar h = \frac{p+1}{n} \tag{3.37}
$$

Variance inflation factor, där $R^2_{X_j \mid X_{-j}}$ är $R^2$ från regressionen av $X_j$ på alla andra prediktorer:

$$
\mathrm{VIF}(\hat\beta_j) = \frac{1}{1 - R^2_{X_j \mid X_{-j}}}, \qquad \mathrm{VIF} > 5 \text{ eller } 10 \Rightarrow \text{problematiskt} \tag{3.38}
$$

## 3.5 Jämförelse med KNN-regression (s. 119–123)

$$
\hat f(x_0) = \frac{1}{K}\sum_{x_i \in \mathcal N_K(x_0)} y_i
$$

Parametrisk regression vinner när den antagna formen är nära sanningen eller när $p$ är stort relativt $n$, eftersom KNN:s grannar blir avlägsna i många dimensioner. Det är samma bias-variance-mönster som i figur 3.20 och i assignment 1.

## Facit från Auto-regressionen (assignment 1)

| Storhet | Värde |
|---|---|
| `mpg ~ horsepower`: $\hat\beta_1$, $R^2$ | $-0.158$, $0.606$ |
| Prediktion vid horsepower 98, 95 % KI, 95 % PI | $24.47$, $[23.97,\ 24.96]$, $[14.81,\ 34.12]$ |
| `mpg ~ alla utom name`: $F$, $R^2$ | $252$, $0.821$ |
| Koefficient för `year` | $0.75$ mpg per år |
| Bästa transformation | $\log(\mathrm{mpg})$ på $\log(\mathrm{hp})$, $\log(\mathrm{weight})$: $R^2_{\text{adj}} = 0.889$ |
