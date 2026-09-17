# MATH 4515 – Cheat sheet, Topic 1: Basic Statistical Methods for Model Construction

Källa: `MATH4515_L1.pdf` (105 sidor). Sidhänvisningar i parentes. Facktermer och notation som i föreläsningen.

---

## 1. Parametrisk modellkonstruktion (s. 2–4)

Tre steg: (1) samla sample data $\{X_1,\dots,X_n\}$, (2) gissa fördelning via histogram, (3) skatta parametrarna. Exempel: AMZN logreturn $\Rightarrow X\sim N(\mu,\sigma^2)$ (s. 3).

**Point estimator** (s. 5): $\hat\theta_n=\hat\theta_n(X_1,\dots,X_n)$ – en formel som mappar ett random sample till ett tal. $\hat\theta_n$ är en **random variable** (s. 6).

Två sätt att få formeln (s. 5): gissa (t.ex. $\hat\mu=\bar X$, $\hat\sigma^2=\frac1n\sum(X_i-\bar X)^2$) eller systematiskt via **method of moments** / **maximum likelihood**.

## 2. Kriterier för bra point estimators (s. 7–8)

| Kriterium | Definition | Sida |
|---|---|---|
| Unbiased | $\mathbb E[\hat\theta_n\mid\theta]=\theta$; annars $\mathrm{Bias}_\theta(\hat\theta_n)=\mathbb E[\hat\theta_n\mid\theta]-\theta$ | 7 |
| Asymptotically unbiased | $\lim_{n\to\infty}\mathbb E[\hat\theta_n\mid\theta]=\theta$ | 11 |
| Consistent | $\lim_{n\to\infty}P(\lvert\hat\theta_n-\theta\rvert>\varepsilon)=0\ \ \forall\varepsilon>0$ | 7 |
| Lowest MSE | $\mathrm{MSE}(\hat\theta_n)=\mathbb E[(\hat\theta_n-\theta)^2]=\mathrm{Var}(\hat\theta_n)+(\mathrm{Bias}_\theta(\hat\theta_n))^2$ | 8 |

- Om unbiased: $\mathrm{MSE}=\mathrm{Var}$ ⇒ bästa unbiased skattaren = minsta varians = **UMVUE** (s. 8).
- Remark: en biased skattare kan ha lägre MSE än en unbiased (s. 8, Example 5).

### Exempel 1–5 (facit)

- **Ex. 1** (s. 9–11): $\bar X$ unbiased. $s^2=\frac1n\sum(X_i-\bar X)^2$ har $\mathbb E[s^2]=\frac{n-1}{n}\sigma^2$ ⇒ biased men asymptotically unbiased. Korrigering: $\hat s^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$ är unbiased. Nyckelfakta i beviset: $\mathbb E[X_i^2]=\sigma^2+\mu^2$, $\mathbb E[\bar X^2]=\sigma^2/n+\mu^2$ (s. 10).
- **Ex. 2** (s. 12–13): $X\sim U[0,\theta]$, $\hat\theta_n=\max(X_i)$. CDF $F(y)=(y/\theta)^n$, pdf $f(y)=ny^{n-1}/\theta^n$, $\mathbb E[\hat\theta_n]=\frac{n}{n+1}\theta$ ⇒ biased, asymptotically unbiased.
- **Ex. 3** (s. 14): $P(\hat\theta_n<\theta-\varepsilon)=\left(\frac{\theta-\varepsilon}{\theta}\right)^n\to0$ ⇒ consistent.
- **Ex. 4** (s. 15–16): $\bar X$ consistent för $\mu$ (via CLT, $\mathrm{Var}(\bar X)=\sigma^2/n$); $\hat\theta_2=X_n$ är **inte** consistent.
- **Ex. 5** (s. 17–19): $\hat\theta_A=2\bar X$, $\hat\theta_B=\frac{n+1}{n}\max(X_i)$, båda unbiased. $\mathrm{Var}(X_i)=\theta^2/12$, $\mathrm{MSE}_A=\frac{\theta^2}{3n}$, $\mathbb E[\hat\theta_B^2]=\frac{(n+1)^2}{n(n+2)}\theta^2$, $\mathrm{MSE}_B=\frac{\theta^2}{n(n+2)}\le\mathrm{MSE}_A$ ⇒ $\hat\theta_B$ bättre.

## 3. Interval estimation / confidence interval (s. 20–28)

$P(\hat\theta_L\le\theta\le\hat\theta_U)=p$, $[\theta_L,\theta_U]$ är ett $(100p)\%$ confidence interval (s. 20).

**Generell metod** (s. 22): (1) point estimator $\hat\theta_n$; (2) fördelningen för $\hat\theta_n$ (exakt eller via CLT); (3) hitta $L,U$ med $P(L\le f(\hat\theta_n,\theta)\le U)=p$; (4) lös olikheten för $\theta$.

Klassiskt fall, känd $\sigma^2$ (s. 21–22): $Z=\frac{\bar X-\mu}{\sqrt{\sigma^2/n}}\sim N(0,1)$, symmetriskt val $z_L=-1.96$, $z_U=1.96$ ⇒
$$\bar X-1.96\sqrt{\sigma^2/n}\ \le\ \mu\ \le\ \bar X+1.96\sqrt{\sigma^2/n}.$$

**Example 6 – Tencent 0700.HK, $P(|\text{return}|>3\%)$** (s. 23–25): $n=2213$, $\hat p=0.1156801$ (formeln på s. 23 skriver $253/2213$ men R-outputen ger $N=256$; $256/2213=0.11568$ stämmer med facit). $X_i\in\{0,1\}$, $\mathrm{Var}(\hat p)=\frac{p(1-p)}{2213}$. Lös $(\hat p-p)^2\le1.96^2\frac{p(1-p)}{2213}$ som andragradsolikhet $ap^2-bp+c\le0$ med $a=1.001736$, $b=2\hat p+0.001735924$, $c=\hat p^2$ ⇒ 95 % CI $[0.101776,\ 0.128313]$.

**Example 7 – HSBC 0005.HK, okänd varians** (s. 26–28): $n=2213$, $\bar r=8.186392\times10^{-5}$, $s=0.01214441$. Antag normal ⇒
$\bar r\sim N(\mu,\sigma^2/n)$, $\chi^2=\frac{(n-1)s^2}{\sigma^2}\sim\chi^2_{n-1}$, oberoende ⇒
$$T=\frac{\bar r-\mu}{s/\sqrt n}=\frac{Z}{\sqrt{\chi^2/(n-1)}}\sim t_{n-1},\quad n-1=2212.$$
98 % CI: $t_U=2.328035$ ⇒ $\mu\in[\bar r\mp2.328035\,s/\sqrt n]=[-0.005191371,\ 0.000682865]$.

Definitioner (s. 27): $\chi^2_n=Z_1^2+\dots+Z_n^2$; $T_n=Z/\sqrt{\chi^2_n/n}$. R: `qt(p,n)`, `qchisq(p,n)` ger kvantiler med $P(T\le T_0)=p$ (s. 28).

## 4. Method of moments (s. 29–34)

Princip: momenten $\mathbb E[X^k]$ är funktioner av $\theta$; via SLLN $\mathbb E[X^k]\approx\frac1n\sum X_i^k$ (s. 30). Lös ekvationssystemet.

- Normal: $\mathbb E[X]=\mu$, $\mathbb E[X^2]=\mu^2+\sigma^2$. Exponential med mean $\theta$: $\mathbb E[X^k]=\theta^k k!$ (s. 29).
- **Ex. 8** (s. 30–31), Tencent logreturn: $\frac1n\sum X_i\approx0.001089745$, $\frac1n\sum X_i^2\approx0.0003827469$ ⇒ $\mu=0.001089745$, $\sigma=0.01953354$ (positiv rot).
- **Ex. 9** (s. 31–33): exponential, $\theta\approx\left(\frac{\sum X_i^k}{n\,k!}\right)^{1/k}$; R: `estimate=(sum(x^k)/(n*factorial(k)))^(1/k)`. Med $\theta=2$, $n=20000$ gav $k=1,2,3$ likvärdig noggrannhet (t.ex. sim. 1: 2.029646, 2.030453, 2.028842). Välj litet $k$: enklare moment, och tunga svansar kan sakna högre moment.
- **Begränsning** (s. 34): $U[0,\theta]$ med data $\{1,2,3\}$ (ca 3500 st vardera) och tre värden $=100$: $\theta/2=\bar X\Rightarrow\theta=4.0554<100$ – inkonsistent med data eftersom medelvärdet styrs av majoriteten.

## 5. Maximum likelihood (s. 35–47)

$$L(\theta_1,\dots,\theta_k)=\prod_{i=1}^n f_X(X_i\mid\theta_1,\dots,\theta_k),\qquad \hat\theta=\arg\max L \quad(\text{s. 35–36})$$
Loglikelihood: $l(\theta)=\ln L(\theta)=\sum_{i=1}^n\ln f_X(X_i\mid\theta)$; samma maximerare eftersom $\ln$ är växande (s. 39).

- **Ex. 10(a)** Poisson (s. 37–38): $L(\lambda)=\lambda^{\sum N_i}e^{-n\lambda}/\prod N_i!$ ⇒ $\hat\lambda_n=\frac1n\sum N_i$.
- **Ex. 10(b)** Exponential $f=\lambda e^{-\lambda x}$ (s. 38–39): $l(\lambda)=n\ln\lambda-\lambda\sum X_i$, $l'=n/\lambda-\sum X_i=0$ ⇒ $\hat\lambda_n=\frac{n}{\sum X_i}$.
- **Ex. 11** Uniform $[0,\theta]$ (s. 40): $L=\theta^{-n}$ för $\theta\ge\max X_i$, annars 0; $L$ avtagande ⇒ $\hat\theta_n=\max(X_1,\dots,X_n)$ (ingen derivata!).

**MLE i R** (s. 41): (1) `fitdistr(x,"normal")` från `MASS` (explicita formler); (2) ad-hoc searching – räkna $l(\theta)$ på ett grid och ta max (funkar alltid, långsamt); (3) `mvnorm.mle(x)`, `mvt.mle(x,v)` från `Rfast`.

- **Ex. 12** (s. 42): `fitdistr(rexp(10000,3),'exponential')` ⇒ rate $3.01353653$ (SE $0.03013537$). 0700.HK normal: mean $0.0010897454$ ($0.0004152315$), sd $0.0195335436$ ($0.0002936130$).
- **Ex. 13** Student-t, $\nu$ (s. 43–44): $f(x\mid\nu)=\frac{\Gamma(\frac{\nu+1}2)}{\sqrt{\pi\nu}\,\Gamma(\frac\nu2)}\left(1+\frac{x^2}{\nu}\right)^{-\frac{\nu+1}2}$. Ingen sluten formel ⇒ grid `v=seq(0.001,10,0.001)`, `which.max(loglik)`. $n=5000$, sann $\nu=3$ ⇒ MLE $3.137$.
- **Ex. 14** Gamma, tvåstegsalgoritm (s. 45–47): $f(x)=\frac{(\lambda x)^\alpha e^{-\lambda x}}{x\Gamma(\alpha)}$,
$$l(\alpha,\lambda)=n\alpha\ln\lambda+(\alpha-1)\sum\ln X_i-n\ln\Gamma(\alpha)-\lambda\sum X_i.$$
  Steg 1: för fixt $\alpha$, $\partial l/\partial\lambda=n\alpha/\lambda-\sum X_i=0\Rightarrow\lambda_\alpha=\frac{n\alpha}{\sum X_i}$. Steg 2: sök $\alpha$ på grid som maximerar $l(\alpha,\lambda_\alpha)$; $(\hat\alpha,\lambda_{\hat\alpha})$ är MLE. Undviker curse of dimensionality. R: `lambda[i]=n*alpha[i]/sum(x)`. Med $\alpha=3,\lambda=1$, $n=20000$: $\hat\alpha=2.947$, $\hat\lambda=0.9871804$. (Obs: andra raden på s. 46 har ett teckenfel, $-(\alpha-1)\sum\ln X_i$; R-koden och första raden använder $+$.)

## 6. MLE:s fyra egenskaper (s. 48–49)

Låt $\hat\theta_n$ uppfylla $l'(\hat\theta_n)=0$. Under regularity conditions:

1. **Asymptotically unbiased**: $\lim_{n\to\infty}\mathbb E[\hat\theta_n]=\theta$ (men *inte nödvändigtvis unbiased* för ändligt $n$).
2. **Consistent**: $\lim P(|\hat\theta_n-\theta|>\varepsilon)=0$.
3. **Asymptotically normal**: $\hat\theta_n\approx N\!\left(\theta,\frac{1}{I(\theta)}\right)$, med **Fisher information**
$$I(\theta)=-n\,\mathbb E\!\left[\frac{\partial^2}{\partial\theta^2}\ln f_X(X\mid\theta)\right].$$
4. **Cramér–Rao bound**: för varje annan *unbiased* skattare $\hat\theta$: $\mathrm{Var}(\hat\theta)\ge\frac{1}{I(\theta)}$ ⇒ MLE har asymptotiskt minsta MSE bland unbiased skattare.

Remark: (3) används för att bygga confidence interval för $\theta$ (s. 49). Egenskap 1 följer ur 3 (s. 51).

### Regularity conditions (s. 50) och var de används i bevisen

| Nr | Villkor | Används till |
|---|---|---|
| (1) | $\ln f_X(x\mid\theta)$ tre gånger deriverbar i $\theta$ | Taylorutveckling av $l'(\theta)$ upp till andra ordningen (s. 53) |
| (2) | $\int\frac{\partial}{\partial\theta}f\,dx=\frac{\partial}{\partial\theta}\int f\,dx$ och samma för $\partial^2/\partial\theta^2$ | $\mathbb E[\text{score}]=0$ (s. 55) och $\mathrm{Var}(\text{score})=-\mathbb E[\partial^2\ln f]=I/n$ (s. 56–57) |
| (3) | $\left\lvert\frac{\partial^3}{\partial\theta^3}\ln f\right\rvert<H(x)$ med $\mathbb E[H(X)]<\infty$ | Resttermen $\frac1n l'''(c)(\hat\theta_n-\theta)^2\to0$ (s. 54) |
| (4) | $-\infty<\mathbb E\!\left[\frac{\partial^2}{\partial\theta^2}\ln f\right]<0$ | $I(\theta)$ ändlig och positiv så man kan dividera med $l''(\theta_{true})$ (s. 55, 57) |

Verktyg (s. 50): **CLT** ($\bar X\approx N(\mu,\sigma^2/n)$) och **SLLN** ($\bar X\to\mu$ a.s.).

### Bevisskisser (s. 51–59)

**Property 2 – consistency** (s. 51–53). $\hat\theta_n$ maximerar $\frac1n l(\theta)=\frac1n\sum\ln f(X_i\mid\theta)\xrightarrow{\text{SLLN}}\mathbb E[\ln f(X\mid\theta)]$. Visa att $\theta_{true}$ är unik maximerare av $\mathbb E[\ln f(X\mid\theta)]$: med $\ln t<t-1$ ($t>0$, $t\ne1$)
$$\mathbb E[\ln f(X\mid\theta)]-\mathbb E[\ln f(X\mid\theta_{true})]=\mathbb E\!\left[\ln\frac{f(X\mid\theta)}{f(X\mid\theta_{true})}\right]<\int\!\Big(\tfrac{f(x\mid\theta)}{f(x\mid\theta_{true})}-1\Big)f(x\mid\theta_{true})dx=1-1=0.$$
(Obs: väntevärdet tas under $f(x\mid\theta_{true})$, inte $f(x\mid\theta)$.) Om $f$ är slät ⇒ $\hat\theta_n\to\theta_{true}$.

**Property 3 – asymptotic normality** (s. 53–57). Taylor: $0=l'(\hat\theta_n)=l'(\theta_{true})+l''(\theta_{true})(\hat\theta_n-\theta_{true})+\frac{l'''(c)}{2}(\hat\theta_n-\theta_{true})^2$ ⇒
$$\hat\theta_n=\theta_{true}-\frac{l'(\theta_{true})+\frac{l'''(c)}{2}(\hat\theta_n-\theta_{true})^2}{l''(\theta_{true})}.$$
- Resttermen: $\frac1n l'''(c)\le\mathbb E[H(X)]<\infty$ och $(\hat\theta_n-\theta_{true})^2\to0$ ⇒ försumbar (s. 54).
- SLLN: $\frac1n l''(\theta_{true})\to\mathbb E[\partial^2\ln f]=-\frac{I(\theta_{true})}{n}$ (s. 55).
- CLT: $\frac{l'(\theta_{true})}{n}=\frac1n\sum\partial_\theta\ln f(X_i\mid\theta)$ approx. normal med mean $\mathbb E[\partial_\theta\ln f]=0$ (villkor (2)) och varians $\frac1n\mathrm{Var}[\partial_\theta\ln f]$ (s. 55).
- $\mathrm{Var}[\partial_\theta\ln f]=\mathbb E[(\partial_\theta\ln f)^2]=-\mathbb E[\partial^2_\theta\ln f]=\frac{I(\theta_{true})}{n}$, via $\partial^2_\theta f=f(\partial_\theta\ln f)^2+f\,\partial^2_\theta\ln f$ och $\int\partial^2_\theta f\,dx=0$ (s. 56–57).
- Alltså $\frac{l'(\theta_{true})}{n}\sim N\!\left(0,\frac{I}{n^2}\right)$ och
$$\hat\theta_n\approx\theta_{true}-\frac{l'(\theta_{true})/n}{-I(\theta_{true})/n}\sim N\!\left(\theta_{true},\ \frac{I/n^2}{(I/n)^2}\right)=N\!\left(\theta_{true},\frac1{I(\theta_{true})}\right).$$

**Property 4 – Cramér–Rao** (s. 58–59). Låt $\hat\theta$ unbiased, $Z=\partial_\theta l(\theta)=\sum\partial_\theta\ln f(X_i\mid\theta)$ (score). Cauchy–Schwarz ($|\rho|\le1$): $\mathrm{Var}(\hat\theta)\ge\frac{[\mathrm{cov}(Z,\hat\theta)]^2}{\mathrm{Var}(Z)}$. $\mathrm{Var}(Z)=n\cdot\frac{I}{n}=I(\theta)$. Derivera $\theta=\int\hat\theta\prod f(x_i\mid\theta)dx$ m.a.p. $\theta$: $1=\mathbb E[\hat\theta Z]$, och $\mathbb E[Z]=0$ ⇒ $\mathrm{cov}(Z,\hat\theta)=1$ ⇒ $\mathrm{Var}(\hat\theta)\ge\frac1{I(\theta)}$.

**Example 15** (s. 60): exponential $f=\lambda e^{-\lambda x}$. $\mathbb E[\partial^2_\lambda(\ln\lambda-\lambda X)]=-1/\lambda^2$ ⇒ $I(\lambda)=n/\lambda^2$, $\mathrm{Var}(\hat\lambda_n)=\lambda^2/n$, bias $\to0$ ⇒ $\mathrm{MSE}(\hat\lambda_n)\approx\frac{\lambda^2}{n}$.

**Flera parametrar** (s. 61): $\hat{\vec\theta}\sim N_k(\vec\theta,\Sigma)$ med $\Sigma=I(\vec\theta)^{-1}$, $a_{ij}=-n\,\mathbb E\!\left[\frac{\partial^2}{\partial\theta_i\partial\theta_j}\ln f(X\mid\vec\theta)\right]$ (slidens första led saknar minustecknet; tolka som $-\mathbb E[\partial^2 l/\partial\theta_i\partial\theta_j]$).

## 7. Model fitting: empirical distribution, percentiler, QQ-plot (s. 62–68)

**Empirical distribution** (s. 62): $F_n(x)=\frac1n\sum_{i=1}^n\mathbf 1_{\{X_i\le x\}}$. Via SLLN $F_n(x)\to F_X(x)$ a.s. (s. 63; $n=100,\dots,10^5$ histogram av $N(0,1)$).

**Percentil** (s. 64): $\pi_p$ löser $F_X(\pi_p)=p$; diskret fall $\pi_p=\sup\{x:F_X(x)<p\}$ eller $\inf\{x:F_X(x)\ge p\}$.

**QQ-plot** (s. 65–67): $X,Y$ samma fördelning $\Leftrightarrow\pi_p^X=\pi_p^Y\ \forall p$. Plotta $(\pi_p^X,\pi_p^Y)$; rät linje med lutning 1 ⇒ samma fördelning. R: `qqplot(x,y)`. Normalitetskoll: $X=\mu+\sigma Z\Rightarrow\pi_p^X=\mu+\sigma\pi_p^Z$ ⇒ QQ-plot mot $N(0,1)$ ska vara en rät linje (lutning $\sigma$, intercept $\mu$).
**Ex. 16** (s. 68): 0005.HK och 0700.HK logreturn ger S-formade QQ-plottar ⇒ normalantagandet håller troligen inte (tyngre svansar).

## 8. Hypothesis testing på normalitet (s. 69–84)

$H_0$: data kommer från $F_X$; $H_1$: inte. Förkasta $H_0$ när p-value $<\alpha$ (kursen använder $\alpha=1\%$).

### Kolmogorov–Smirnov (s. 69–72, 76–77)
$$D_n=\sup_{x}\lvert F_n(x)-F_X(x)\rvert,\qquad\text{Reject }H_0\Leftrightarrow D_n>D^*.$$
Manuell beräkning (s. 76): sortera $X_{1}\le\dots\le X_{n}$, $X_0=-\infty$, $X_{n+1}=+\infty$, $F_X(X_0)=0$, $F_X(X_{n+1})=1$:
$$D=\max_{i=1,\dots,n+1}\max\big(\lvert F_n(X_{i-1})-F_X(X_{i-1})\rvert,\ \lvert F_n(X_{i-1})-F_X(X_i)\rvert\big).$$
R (s. 71): `ks.test(x,'pnorm',mean=MLEs$estimate["mean"],sd=MLEs$estimate["sd"])`; lägg till `1e-16*rnorm(n)` för att undvika ties. Manuell kod på s. 77 ger $D=0.04737089$ för 0700.HK.

**Ex. 17** (s. 71–72), normal, 2011–2019:

| Aktie | $D$ | p-value | Slutsats |
|---|---|---|---|
| 0005.HK | 0.06192 | $8.535\times10^{-8}$ | reject $H_0$: ej normal |
| 0700.HK | 0.047371 | $9.719\times10^{-5}$ | reject $H_0$: ej normal |

**General t-distribution** (s. 73): $X=\mu+\lambda T_\nu\sim t_\nu(\mu,\lambda)$, $\mathbb E[X]=\mu$, $\mathrm{Var}(X)=\frac{\nu}{\nu-2}\lambda^2$ ($\nu>2$); litet $\nu$ ⇒ tyngre svans. Fit: `mvt.mle(x,v=df)` på grid `df=seq(2,8,0.001)`, välj df med max `$loglik`; $m$=`$location`, $s$=`sqrt($scatter[1,1])`, testa $T=(x-m)/s$ mot `'pt'` (s. 74).

**KS mot t** (s. 75):

| Aktie | $m$ | $s$ | $\nu$ (dfmax) | $D$ | p-value |
|---|---|---|---|---|---|
| 0005.HK | 0.0002001957 | 0.008415141 | 3.631 | 0.019484 | 0.3702 |
| 0700.HK | 0.001117649 | 0.01526518 | 4.937 | 0.01842 | 0.4406 |

Accept $H_0$ – t-fördelning verkar bättre, men det bevisar inte att avkastningen *är* t-fördelad.

### Anderson–Darling (s. 78–84)
Viktad kvadratisk distans med fokus på svansarna. Oviktad $\mathbb E[(F_n-F_X)^2]$ ger för lite vikt i svansen (s. 78). Under $H_0$: $nF_n(x)\sim\mathrm{Bin}(n,F_X(x))$ ⇒ $\mathrm{Var}(F_n(x))=\frac{F_X(x)(1-F_X(x))}{n}$ (s. 79) ⇒ vikt $\phi(x)=\frac{n}{F_X(x)(1-F_X(x))}$, som är störst när $F_X\approx0$ eller $1$ (s. 80):
$$D_n^*=n\int_{-\infty}^\infty\frac{(F_n(x)-F_X(x))^2}{F_X(x)(1-F_X(x))}f_X(x)\,dx.$$
Beräkning (s. 81–82): under $H_0$ är $U=F_X(X)\sim U[0,1]$; med sorterad data och $u_k=F_X(X_{(k)})$:
$$D_n^*=-\sum_{k=1}^n\frac{2k-1}{n}\big[\ln u_k+\ln(1-u_{n+1-k})\big]-n.$$
R (s. 83): `library(goftest)`; `ad.test(x,"pnorm",mean=...,sd=...)`.

**Ex. 18** (s. 83–84):

| Aktie | Normal: $A_n$, p | t: $A_n$, p |
|---|---|---|
| 0005.HK | 20.141, $2.711\times10^{-7}$ | 0.36482, 0.8828 |
| 0700.HK | 10.106, $5.818\times10^{-6}$ | 0.82584, 0.4628 |

Normal förkastas ($p<0.01$); ingen evidens mot t-fördelning.

## 9. Bayesian analysis för parameterskattning (s. 85–88)

Motiv: MLE kräver stort sample; Bayes kombinerar data med **prior** $\pi(\theta)$ och kan uppdateras. Flat prior = uniform över möjliga $\theta$ (används i BIC) (s. 86).

**Posterior** (Bayes' rule, s. 87):
$$\pi(\theta\mid X_1,\dots,X_n)=\frac{\left[\prod_{i=1}^n f_X(X_i\mid\theta)\right]\pi(\theta)}{\int\left[\prod_{i=1}^n f_X(X_i\mid\theta)\right]\pi(\theta)\,d\theta}.$$
Ger en *fördelning* för $\theta$, inte en punktskattning; konvergerar mot sanna värdet när $n\to\infty$.

**Ex. 19** (s. 88): exponential $\lambda e^{-\lambda x}$, prior $\pi(k)=0.2$, $k=1,\dots,5$ ⇒
$$\pi(\lambda\mid X)=\frac{\lambda^n e^{-\lambda\sum X_i}}{\sum_{k=1}^5 k^n e^{-k\sum X_i}},\quad\lambda=1,\dots,5.$$

## 10. AIC – Akaike Information Criterion (s. 89–96)

**Kullback–Leibler distance** mellan sann $f_X$ och modell $g_X(\cdot\mid\theta)$ (s. 89):
$$D=\int(\ln f_X(x)-\ln g_X(x\mid\theta))f_X(x)\,dx=\mathbb E[\ln f_X(X)-\ln g_X(X\mid\theta)]\ \ge0$$
($D\ge0$ via $\ln x\le x-1$, s. 90). Minimera $D$ ⇔ maximera $\mathbb E[\ln g_X(X\mid\theta)]\approx\frac1n l(\theta)$; med $\theta=\hat\theta_n$ (MLE) (s. 90–91). AIC = MLE utvidgat till val av *både* modell och parametrar.

Bias-korrektion (s. 92): $\mathbb E[\frac1n l(\hat\theta_n)]\approx\mathbb E[\ln g_X(X\mid\hat\theta_n)]+\frac kn$, $k$ = antal parametrar ⇒ unbiased skattare $\frac1n l(\hat\theta_n)-\frac kn=-\frac1{2n}(-2l(\hat\theta_n)+2k)$:
$$\boxed{\mathrm{AIC}=-2\,l(\hat\theta_n)+2k}\qquad\text{välj modellen med lägst AIC.}$$
R: `logLik(fitdistr(x,"dist"))` ger max loglikelihood (s. 94).

**Ex. 20** (s. 93–94), $10^6$ exponential-data, $\lambda=0.025$:

| Modell | MLE | max loglik | AIC |
|---|---|---|---|
| Exponential | $\lambda=0.0250156$ | $-4688257$ | **9376516** |
| Normal | $\mu=39.975113$, $\sigma=39.98147$ | $-5107355$ | 10214713 |
| Log-normal | $\mu=3.110918$, $\sigma=1.2829$ | $-4778980$ | 9557964 |

**Ex. 21** (s. 95–96), 0700.HK logreturn, $k=2$ (normal) resp. $k=3$ (general t): `AIC=-2*loglik_value+2*3`.

| Modell | MLE | AIC |
|---|---|---|
| Normal | $\mu=0.0010897454$, $\sigma=0.0195335436$ | $-11134.84$ |
| General t | $\mu=0.001117649$, $\lambda=0.01526518$, $\nu=4.937$ | **$-11288.83$** |

## 11. BIC – Bayesian Information Criterion (s. 97–104)

Setup: $N$ modeller $M_i$ med parametrar $\vec\theta_i\in\mathbb R^{m_i}$, prior $P(M=M_i)=1/N$, flat prior $\pi(\vec\theta_i)=c_i$ (s. 97). Välj modellen med högst posterior $P(M_i\mid X)\propto f_{\vec X}(X\mid M_i)=c_i\int L(\vec\theta_i)\,d\vec\theta_i$ (s. 98).

Härledning (s. 99–104): Taylor av $l$ kring MLE $\vec\theta_i^*$ (gradient $=0$): $l(\vec\theta_i)\approx l(\vec\theta_i^*)-\frac12(\vec\theta_i-\vec\theta_i^*)^T\tilde H(\vec\theta_i-\vec\theta_i^*)$ med $\tilde H=-H$ positivt definit. Diagonalisera $\tilde H=UDU^T$, Gaussintegral $\int e^{-\lambda_k y^2/2}dy=\sqrt{2\pi/\lambda_k}$ ⇒
$$f_{\vec X}(X\mid M_i)=c_i\,L(\vec\theta_i^*)\frac{(2\pi)^{m_i/2}}{(\det\tilde H)^{1/2}}.$$
Med SLLN: $l(\vec\theta_i^*)\approx n\mathbb E[\ln f_X]$ och $\det\tilde H=n^{m_i}\det A$ ⇒ $\ln\det\tilde H=m_i\ln n+\ln\det A$. Stryk termer oberoende av $n$:
$$\ln f_{\vec X}(X\mid M_i)\approx l(\vec\theta_i^*)-\frac{m_i}{2}\ln n=-\tfrac12\big(m_i\ln n-2l(\vec\theta_i^*)\big)$$
$$\boxed{\mathrm{BIC}=-2\,l(\hat\theta)+m_i\ln n}\qquad\text{välj lägst BIC.}$$
Skillnad mot AIC: penalty $m_i\ln n$ i stället för $2m_i$ (hårdare för stort $n$) (s. 104).

## 12. R-kommandon i sammanfattning

| Uppgift | Kommando | Sida |
|---|---|---|
| MLE normal/exp/Poisson | `library(MASS); fitdistr(x,"normal")` | 41–42 |
| Max loglikelihood | `logLik(fitdistr(x,"dist"))` | 94 |
| MLE multivariat t | `library(Rfast); mvt.mle(x,v=df)` (`$loglik`, `$location`, `$scatter`) | 41, 74 |
| Kvantiler | `qt(p,df)`, `qchisq(p,df)` | 28 |
| Slump | `rexp(n,rate)`, `rt(n,df)`, `rgamma(n,shape,rate)`, `rnorm` | 32, 44, 47 |
| QQ-plot | `qqplot(x,y)`, `qqnorm` | 65 |
| KS-test | `ks.test(x,'pnorm',mean=,sd=)`, `ks.test(T,'pt',df=)` | 71, 74 |
| AD-test | `library(goftest); ad.test(x,"pnorm",mean=,sd=)` | 83 |

## 13. Vanliga fel / att komma ihåg

- **$I(\theta)$ innehåller faktorn $n$ i denna kurs** (s. 49): $I(\theta)=-n\mathbb E[\partial^2_\theta\ln f]$. Därför: $\mathrm{Var}(\partial_\theta\ln f(X_i\mid\theta))=I/n$ (en term av score), $\mathrm{Var}(l'(\theta))=\mathrm{Var}(Z)=I$ (s. 58), $\mathrm{Var}(l'(\theta)/n)=I/n^2$ (s. 57), och $\mathrm{Var}(\hat\theta_n)\approx1/I$ – redan "per $n$ observationer".
- **Maximera $l(\theta)$ eller $l(\theta)/n$** ger samma $\hat\theta_n$; $l/n$ används i bevisen för att SLLN ska gälla ($\frac1n l\to\mathbb E[\ln f]$, $\frac1n l''\to-I/n$).
- **MLE behöver inte vara unbiased för ändligt $n$** (s. 48): t.ex. $\max X_i$ för uniform har $\mathbb E=\frac{n}{n+1}\theta$; $s^2$ (MLE av $\sigma^2$) har $\mathbb E=\frac{n-1}{n}\sigma^2$.
- **Cramér–Rao gäller bara unbiased skattare** (s. 49, 58). En biased skattare kan ha $\mathrm{MSE}<1/I$.
- **$\mathrm{MSE}=\mathrm{Var}+\mathrm{Bias}^2$**, inte $\mathrm{Var}+\mathrm{Bias}$ (s. 8). Lägre MSE kan slå unbiasedness (Ex. 5).
- **$\ln t<t-1$** ($t\ne1$) är nyckeln både i consistency-beviset (s. 52) och $D_{KL}\ge0$ (s. 90); väntevärdet tas alltid under den *sanna* tätheten.
- **MLE via derivata funkar inte när stödet beror på $\theta$** (uniform, Ex. 11) – resonera om monotonitet i stället.
- **Method of moments** kan ge skattningar oförenliga med data (s. 34); välj lågt $k$ (s. 33).
- **CI för proportion** kräver att man löser en andragradsolikhet i $p$ när variansen $p(1-p)/n$ innehåller $p$ (Ex. 6); CI för $\mu$ med okänd $\sigma$ använder $t_{n-1}$, inte $N(0,1)$ (Ex. 7).
- **Hypotestest**: reject $H_0$ om p-value $<\alpha$. Stort p-value betyder "ingen evidens mot", inte "bevisat" (s. 75). KS är svag i svansarna – använd AD (s. 78).
- **Antal parametrar** i AIC/BIC: normal $k=2$, general t $k=3$ (s. 95). Lägst score vinner. AIC-penalty $2k$, BIC-penalty $k\ln n$.
- **fitdistr-output**: första raden = MLE, parentesen = standard error (s. 42).

## 14. Vad som saknar kod i `code/MATH_4515.ipynb`

Notebooken innehåller i dagsläget en enda ofullständig cell (`load(file=)`) – ingenting från anteckningen är implementerat ännu. Data finns som `code/0005_HK.xlsx` och `code/0700_HK.xlsx`. Kandidater att koda, i föreläsningens ordning:

1. Läsa in xlsx, beräkna logreturn, histogram (s. 3).
2. Ex. 6: $\hat p$ och 95 % CI via andragradsolikheten (s. 23–25).
3. Ex. 7: 98 % CI för $\mu$ med $t_{2212}$ (s. 26–28); CI för $\sigma^2$ via `qchisq` (nämns som remark).
4. Ex. 8–9: method of moments (normal på Tencent, exponential-simulering med $k=1,2,3$) (s. 30–33).
5. Ex. 12: `fitdistr` på exponential-simulering och 0700.HK (s. 42).
6. Ex. 13: ad-hoc grid search för $\nu$ i student-t (s. 44).
7. Ex. 14: gamma tvåstegsalgoritm med $\lambda_\alpha=n\alpha/\sum X_i$ (s. 47).
8. Empirical CDF och QQ-plottar för 0005.HK/0700.HK (s. 63–68).
9. Ex. 17: KS-test mot normal och mot general t (`mvt.mle`) samt manuell $D$-beräkning (s. 71–77).
10. Ex. 18: Anderson–Darling (`goftest::ad.test`), gärna även formeln på s. 82 manuellt.
11. Ex. 19: posterior för diskret prior (s. 88).
12. Ex. 20–21: AIC för exponential/normal/lognormal och normal vs general t (s. 93–96); BIC-motsvarighet (s. 104).
