# ISLP kap. 4, övning 2 – LDA:s diskriminantfunktion

**Visa:** att klassificera till det $k$ som maximerar $p_k(x)$ (4.17) är samma sak som att maximera

$$\delta_k(x) = x\,\frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + \log \pi_k \qquad (4.18)$$

givet att $X \mid Y=k \sim N(\mu_k, \sigma^2)$ med **samma** $\sigma^2$ för alla klasser (s. 147–148).

$$p_k(x) = \frac{\pi_k \frac{1}{\sqrt{2\pi}\sigma}\exp\!\left(-\frac{1}{2\sigma^2}(x-\mu_k)^2\right)}{\sum_{l=1}^K \pi_l \frac{1}{\sqrt{2\pi}\sigma}\exp\!\left(-\frac{1}{2\sigma^2}(x-\mu_l)^2\right)}$$

---

## Strategin i en mening

Vi jämför klasser **för ett fixt $x$**. Allt som inte beror på $k$ påverkar inte vilket $k$ som vinner och kan strykas. Monotona transformationer, som $\log$, ändrar inte heller vem som vinner.

## Steg 1: Nämnaren beror inte på $k$

Nämnaren summerar över alla $l$. Den är samma tal för varje $k$, så

$$\arg\max_k p_k(x) = \arg\max_k \; \pi_k \tfrac{1}{\sqrt{2\pi}\sigma}\exp\!\left(-\tfrac{1}{2\sigma^2}(x-\mu_k)^2\right).$$

## Steg 2: Ta logaritmen

$\log$ är strikt växande, så arg max bevaras:

$$\log \pi_k - \log(\sqrt{2\pi}\sigma) - \frac{(x-\mu_k)^2}{2\sigma^2}$$

Termen $\log(\sqrt{2\pi}\sigma)$ beror inte på $k$, eftersom $\sigma$ är gemensam. Stryk den.

## Steg 3: Utveckla kvadraten

$$-\frac{(x-\mu_k)^2}{2\sigma^2} = -\frac{x^2}{2\sigma^2} + \frac{x\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2}$$

$-\frac{x^2}{2\sigma^2}$ är samma för alla $k$. Stryk den också. Det som återstår är exakt $\delta_k(x)$. ∎

---

## Var antagandet $\sigma_k = \sigma$ används

Det används på **två** ställen: i steg 2 (konstanten $\frac{1}{\sqrt{2\pi}\sigma}$) och i steg 3 (termen $x^2/2\sigma^2$). Om varianserna skiljer sig mellan klasserna kan ingen av dem strykas. Då blir $\delta_k$ **kvadratisk** i $x$, och det är precis övning 3 (QDA).

## Vanliga misstag

- Att skriva att $p_k(x) = \delta_k(x)$. Det är **inte** samma tal, bara samma arg max.
- Att glömma att motivera varför logaritmen är tillåten (strikt växande).
- Att stryka $x^2$-termen utan att säga att det beror på gemensam $\sigma^2$.
