# Värdering av ränteswap – två metoder

**Uppgift (T6, Ex. 1):** $N = 100\,000$. Investeraren **tar emot flytande** 6-månadersränta och **betalar fast** 8 % nominell, halvårsvis. Betalningar sker om 0.25, 0.75 och 1.25 år. Den senast fastställda flytande räntan är 9 % nominell.

| $T_i$ | 0.25 | 0.75 | 1.25 |
|---|---|---|---|
| $B(0;T_i)$ | 0.99 | 0.96 | 0.93 |

Räntor per period: fast $c = 0.08/2 = 0.04$, känd flytande $r_1 = 0.09/2 = 0.045$.

$$V_{\text{swap}} = \text{PV(det man tar emot)} - \text{PV(det man betalar)} = V_{fl} - V_{fix}$$

---

## (a) Bond price approach

**Idé:** Lägg till ett fiktivt utbyte av principalen $N$ vid sista betalningen. Det ändrar inte swappens värde, eftersom båda parter betalar $N$ till varandra och det tar ut sig. Då är swappen detsamma som

- **lång** en flytande obligation (floating rate note) och
- **kort** en fast kupongobligation.

### Fasta benet: en vanlig kupongobligation

$$
\begin{aligned}
B_{fix} &= cN\sum_{i=1}^{3} B(0;T_i) + N\,B(0;T_3) \\
&= 4000\,(0.99+0.96+0.93) + 100\,000\cdot 0.93 \\
&= 11\,520 + 93\,000 = 104\,520
\end{aligned}
$$

### Flytande benet: tricket

En flytande obligation är värd **exakt par ($N$) direkt efter varje reset-dag**. Kupongen sätts då till marknadsräntan för perioden, så diskontering och kupong tar ut varandra.

Alltså: precis vid nästa betalning ($T_1 = 0.25$) är obligationen värd $N$ (efter reset) plus den redan kända kupongen $r_1 N$. Diskontera det tillbaka:

$$
B_{fl} = (N + r_1 N)\,B(0;T_1) = 104\,500 \cdot 0.99 = 103\,455
$$

De framtida okända flytande räntorna behövs inte alls.

### Swapvärde

$$
V = B_{fl} - B_{fix} = 103\,455 - 104\,520 = \boxed{-1065}
$$

---

## (b) Forward rate approach

**Idé:** Se swappen som en serie FRA:er. Varje okänd flytande ränta ersätts med den **forwardränta** som idag gäller för perioden. Därefter diskonteras varje periods **nettoflöde** $N(\text{flytande} - \text{fast})$.

### Steg 1: forwardräntor per period ur diskonteringsfaktorerna

$$
1 + f(T_{i-1},T_i) = \frac{B(0;T_{i-1})}{B(0;T_i)}
$$

| Period | Flytande ränta (per halvår) |
|---|---|
| $0 \to 0.25$ | $r_1 = 0.045$ (redan känd) |
| $0.25 \to 0.75$ | $f_2 = 0.99/0.96 - 1 = 0.03125$ |
| $0.75 \to 1.25$ | $f_3 = 0.96/0.93 - 1 = 0.032258$ |

Forwardräntorna är redan **räntor per period**. Dela inte med 2.

### Steg 2: diskontera nettoflödena

| $T_i$ | Netto $N(f_i - c)$ | $B(0;T_i)$ | PV |
|---|---|---|---|
| 0.25 | $100\,000(0.045-0.04) = 500$ | 0.99 | 495.00 |
| 0.75 | $100\,000(0.03125-0.04) = -875$ | 0.96 | −840.00 |
| 1.25 | $100\,000(0.032258-0.04) = -774.19$ | 0.93 | −720.00 |

$$
V = 495 - 840 - 720 = \boxed{-1065}
$$

---

## Varför blir det samma?

$N f_i B(0;T_i) = N\big(B(0;T_{i-1}) - B(0;T_i)\big)$. Summan av flytande flöden från period 2 och framåt **teleskoperar** därför till $N\big(B(0;T_1) - B(0;T_3)\big)$. Lägger man till principalen $N B(0;T_3)$ blir det $N B(0;T_1)$, alltså par vid $T_1$. Det är exakt tricket i (a).

| | (a) Bond price | (b) Forward rate |
|---|---|---|
| Synsätt | lång FRN, kort fast obligation | portfölj av FRA:er |
| Behöver forwardräntor? | nej | ja |
| Principal | läggs till fiktivt | behövs inte |
| Resultat | −1065 | −1065 |

**Tolkning:** Värdet är negativt för investeraren. Den fasta räntan 8 % ligger över de implicita forwardräntorna (≈ 6.25 % och 6.45 % nominellt), så investeraren betalar mer än vad som förväntas komma in.
