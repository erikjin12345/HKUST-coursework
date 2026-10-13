# Portföljval med vektorer och en riskfri tillgång

FINA 3103, HW1 Part B. Siffrorna är kontrollerade i `FINA 3103/code/html_checks/tangency_check.py`.

## 1. Notation

$n$ riskfyllda tillgångar plus en riskfri tillgång med räntan $r_f$.

| Symbol | Dimension | Betydelse |
|---|---|---|
| $\boldsymbol\mu$ | $\mathbb R^n$ | förväntad avkastning för de riskfyllda tillgångarna |
| $\Sigma$ | $\mathbb R^{n\times n}$ | kovariansmatris för de riskfyllda tillgångarna |
| $\mathbf 1$ | $\mathbb R^n$ | vektor med bara ettor |
| $\mathbf w$ | $\mathbb R^n$ | vikter i de riskfyllda tillgångarna |
| $w_{rf}$ | skalär | vikt i den riskfria tillgången |

**$r_f$ ingår inte i $\boldsymbol\mu$ eller $\Sigma$.** Den riskfria tillgången har varians 0 och kovarians 0 med allt. Läggs den in i $\Sigma$ får matrisen en rad och en kolumn med bara nollor och blir singulär:

$$
\begin{pmatrix} 0 & 0 & 0 \\ 0 & \sigma_S^2 & \sigma_{SB} \\ 0 & \sigma_{SB} & \sigma_B^2 \end{pmatrix}, \qquad \det = 0 \;\Rightarrow\; \Sigma^{-1} \text{ finns inte.}
$$

## 2. Överavkastning

$$
r_f\mathbf 1 = \begin{pmatrix} r_f \\ \vdots \\ r_f \end{pmatrix},
\qquad
\boldsymbol\mu - r_f\mathbf 1 = \begin{pmatrix} E[r_1] - r_f \\ \vdots \\ E[r_n] - r_f \end{pmatrix}
$$

Med S och B:

$$
\boldsymbol\mu - r_f\mathbf 1 = \begin{pmatrix} 0.10 \\ 0.06 \end{pmatrix} - 0.03\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0.07 \\ 0.03 \end{pmatrix}
$$

## 3. Vikterna

Hela portföljen summerar till 1, men den riskfyllda delen $\mathbf w$ behöver inte göra det:

$$
\underbrace{\mathbf 1^\top \mathbf w}_{=\,y} + w_{rf} = 1
\qquad\Longrightarrow\qquad
w_{rf} = 1 - \mathbf 1^\top \mathbf w
$$

- $\mathbf 1^\top \mathbf w = y$ är andelen i riskfyllda tillgångar.
- $w_{rf} > 0$ betyder att man lånar ut, och $w_{rf} < 0$ att man lånar.
- Bara tangentportföljen $P^*$ normeras så att $\mathbf 1^\top \mathbf w^* = 1$.

## 4. Förväntad avkastning och varians

$$
\begin{aligned}
E[r_C] &= \mathbf w^\top\boldsymbol\mu + (1 - \mathbf 1^\top\mathbf w)\,r_f = r_f + \mathbf w^\top(\boldsymbol\mu - r_f\mathbf 1) \\[4pt]
\sigma_C^2 &= \mathbf w^\top \Sigma\, \mathbf w
\end{aligned}
$$

Det är vektorversionen av $E[r_C] = r_f + y\,(E[r_{P^*}] - r_f)$. Termen $r_f$ läggs inte till ovanpå portföljen. Den kommer från att $(1-\mathbf 1^\top\mathbf w)\,r_f$ bryts ut ur det viktade medelvärdet.

## 5. Optimering utan bivillkor

Eftersom $w_{rf}$ tar upp resten behövs inget villkor på $\mathbf w$:

$$
\max_{\mathbf w}\; U(\mathbf w) = r_f + \mathbf w^\top(\boldsymbol\mu - r_f\mathbf 1) - \frac{A}{2}\,\mathbf w^\top\Sigma\,\mathbf w
$$

$$
\nabla U = (\boldsymbol\mu - r_f\mathbf 1) - A\,\Sigma\,\mathbf w = \mathbf 0
\qquad\Longrightarrow\qquad
\boxed{\;\mathbf w = \frac1A\,\Sigma^{-1}(\boldsymbol\mu - r_f\mathbf 1)\;}
$$

## 6. Två steg = ett steg

Sätt $\mathbf z = \Sigma^{-1}(\boldsymbol\mu - r_f\mathbf 1)$.

| Steg | Formel | Beror på $A$? |
|---|---|---|
| 1. Tangentportföljen $P^*$ | $\mathbf w^* = \dfrac{\mathbf z}{\mathbf 1^\top \mathbf z}$ | nej |
| 2. Andel i $P^*$ | $y^* = \dfrac{E[r_{P^*}] - r_f}{A\,\sigma_{P^*}^2} = \dfrac{\mathbf 1^\top \mathbf z}{A}$ | ja |
| Hela portföljen | $\mathbf w = y^*\,\mathbf w^* = \dfrac{\mathbf z}{A}$ | ja |

Riktningen $\mathbf z$ är densamma för alla investerare, och $A$ skalar bara längden. Det är separationsegenskapen.

## 7. Med uppgiftens siffror

$$
\Sigma = \begin{pmatrix} 0.0324 & 0.0045 \\ 0.0045 & 0.01 \end{pmatrix},
\qquad
\mathbf z = \Sigma^{-1}\begin{pmatrix} 0.07 \\ 0.03 \end{pmatrix} = \begin{pmatrix} 1.8601 \\ 2.1630 \end{pmatrix},
\qquad
\mathbf 1^\top\mathbf z = 4.0231
$$

| | $\mathbf w$ | $\mathbf 1^\top\mathbf w = y^*$ | $w_{rf}$ |
|---|---|---|---|
| $P^*$: $\mathbf z / 4.0231$ | $(0.4624,\ 0.5376)$ | 1 | 0 |
| Elaine, $A = 3$: $\mathbf z / 3$ | $(0.6200,\ 0.7210)$ | 1.3410 | $-0.3410$ |
| Chen, $A = 1.5$: $\mathbf z / 1.5$ | $(1.2401,\ 1.4420)$ | 2.6820 | $-1.6820$ |

$\mathbf 1^\top\mathbf z = 4.0231$ är också den övre gränsen för $A$ i (c): den som har större $A$ än så vill inte låna ens till $r_f$.

## 8. Utan riskfri tillgång

Då finns inget $w_{rf}$ som tar upp resten, och man måste lägga till bivillkoret $\mathbf 1^\top\mathbf w = 1$, till exempel med en Lagrange-multiplikator:

$$
\max_{\mathbf w}\; \mathbf w^\top\boldsymbol\mu - \frac A2\,\mathbf w^\top\Sigma\,\mathbf w
\quad\text{s.t.}\quad \mathbf 1^\top\mathbf w = 1
$$

Mixen beror då på $A$, och separationen gäller inte längre.

## 9. I kod

```python
import numpy as np
mu = np.array([0.10, 0.06])
Sigma = np.array([[0.0324, 0.0045], [0.0045, 0.01]])
rf = 0.03

z = np.linalg.solve(Sigma, mu - rf)   # Sigma^-1 (mu - rf 1); "mu - rf" broadcasts
w_star = z / z.sum()                  # tangency portfolio P*
w = z / 3                             # Elaine's risky weights
w_rf = 1 - w.sum()                    # rest in the risk-free asset
```
