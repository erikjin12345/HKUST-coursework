# Scratch-sidor

Lägg en `.md`-fil i `web/content/` så dyker den upp i menyn under **Scratch**. Filerna renderas med GitHub-markdown och KaTeX. Repots egna filer, till exempel varje kurs `CHEATSHEET.md`, listas under respektive kursnamn.

## LaTeX

Inline: $D_{Mod} = D_{Mac}/(1+i)$. Display:

$$
\frac{P(i_0+\varepsilon) - P(i_0)}{P(i_0)} \approx -\varepsilon\, D_{Mod} + \frac{\varepsilon^2}{2}\, C_{Mod}
$$

Flerradigt med `aligned`:

$$
\begin{aligned}
\mathbb{E}\big[(f - \hat f)^2\big] &= \big(f - \mathbb{E}[\hat f]\big)^2 + \mathbb{E}\big[(\hat f - \mathbb{E}[\hat f])^2\big] \\
&= \text{Bias}^2 + \text{Var}
\end{aligned}
$$

## Tabeller och kod

| $p$ | KNN bäst $K$ | MSE |
|---|---|---|
| 1 | 9 | 0.032 |
| 20 | 9 | 0.384 |

```python
def pv_annuity(C, r, n):
    return C / r * (1 - (1 + r) ** -n)
```
