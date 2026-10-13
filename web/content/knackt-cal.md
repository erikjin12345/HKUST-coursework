# Knäckt CAL: olika ränta för utlåning och lån

FINA 3103, HW1 Part B (c). Siffrorna och figurerna kommer från `FINA 3103/code/html_checks/kink_plot.py`.

## 1. Uppställning

Man lånar ut till $r_f = 3\%$ men lånar till $r_B = 6\%$. $P^*$ är tangentportföljen från (b):

$$
E_P = 0.0785, \qquad \sigma_P = 0.1098, \qquad \sigma_P^2 = 0.012054
$$

Med andelen $y$ i $P^*$ är vikten i den riskfria tillgången $1-y$:

- $y \le 1$ ger $1 - y \ge 0$, så man **lånar ut** och tjänar $r_f$.
- $y > 1$ ger $1 - y < 0$, så man **lånar** och betalar $r_B$.

Räntan beror alltså på tecknet på $1-y$:

$$
r(y) = \begin{cases} r_f, & y \le 1 \\ r_B, & y > 1 \end{cases}
$$

## 2. Avkastning och nytta

$$
E[r_C] = (1-y)\,r(y) + y\,E_P = r(y) + y\,\big(E_P - r(y)\big), \qquad \sigma_C = y\,\sigma_P
$$

Insatt i $U = E[r] - \tfrac12 A\sigma^2$:

$$
U(y) = \begin{cases}
U_L(y) = r_f + y\,(E_P - r_f) - \tfrac12 A\sigma_P^2\,y^2, & y \le 1 \\[4pt]
U_B(y) = r_B + y\,(E_P - r_B) - \tfrac12 A\sigma_P^2\,y^2, & y > 1
\end{cases}
$$

$U$ följer alltså två olika parabler, och båda har samma krökning $-A\sigma_P^2$.

## 3. Varför det blir en knäck

**Kontinuitet i $y = 1$.** Båda grenarna ger samma värde, eftersom $r(y)$ multipliceras med $1-y = 0$:

$$
U_L(1) = U_B(1) = E_P - \tfrac12 A\sigma_P^2
$$

**Derivatorna skiljer sig:**

$$
U_L'(y) = (E_P - r_f) - A\sigma_P^2\,y, \qquad U_B'(y) = (E_P - r_B) - A\sigma_P^2\,y
$$

$$
U_L'(1) - U_B'(1) = r_B - r_f = 0.03
$$

Lutningen faller alltså med $r_B - r_f$ i $y = 1$. Varje extra krona i $P^*$ som tas från den egna kassan kostar $r_f$ i utebliven ränta. Varje extra krona som lånas kostar $r_B$. Är räntorna lika blir knäcken noll, och man är tillbaka i (b).

![U(y) för tre investerare](/repo/web/content/knackt-cal/utility.png)

Heldragen linje är $U(y)$. Prickad är $U_L$ förlängd förbi $y=1$ och streckad är $U_B$. Till vänster om $y=1$ följer $U$ den prickade parabeln, och till höger hoppar den ned till den streckade.

## 4. Härledning av $y^*$

Maximera varje gren för sig med förstaordningsvillkoret.

**Utlåningsgrenen.** $U_L'(y) = 0$ ger

$$
y_L = \frac{E_P - r_f}{A\,\sigma_P^2}
$$

**Lånegrenen.** $U_B'(y) = 0$ ger

$$
y_B = \frac{E_P - r_B}{A\,\sigma_P^2}
$$

Eftersom $r_B > r_f$ gäller alltid $y_B < y_L$.

En topp är bara giltig om den ligger på sin egen gren. $U$ är konkav, eftersom båda parablerna är konkava och lutningen bara faller i knäcken. Därför finns exakt tre fall:

| Fall | Villkor | $y^*$ | Tolkning |
|---|---|---|---|
| 1 | $y_L \le 1$ | $y_L$ | lånar ut |
| 2 | $y_B \ge 1$ | $y_B$ | lånar |
| 3 | $y_B < 1 < y_L$ | $1$ | allt i $P^*$, ingen riskfri position |

**Fall 3 i detalj.** Varken $y_L$ eller $y_B$ ligger på sin egen gren:

- $U_L'(1) > 0$: man vill öka $y$ upp till 1 så länge man lånar ut.
- $U_B'(1) < 0$: man vill inte gå förbi 1 när man måste låna.

Toppen hamnar därför exakt i knäcken. Formellt är $y=1$ optimalt när $0$ ligger i intervallet $[U_B'(1),\ U_L'(1)]$, det vill säga i subgradienten.

## 5. Intervallet för $A$

Fall 3, uttryckt i $A$:

$$
U_B'(1) \le 0 \le U_L'(1)
\iff
E_P - r_B \le A\sigma_P^2 \le E_P - r_f
$$

$$
\boxed{\;\frac{E_P - r_B}{\sigma_P^2} \le A \le \frac{E_P - r_f}{\sigma_P^2}\;}
\qquad\Longrightarrow\qquad
1.5343 \le A \le 4.0230
$$

- $A > 4.0230$: lånar ut.
- $A < 1.5343$: lånar till 6 %.
- Däremellan: exakt $y = 1$.

**Intervallet gäller åt båda hållen:**

$$
y^* = 1 \iff 1.5343 \le A \le 4.0230
$$

- **$A$ i intervallet ⇒ $y^* = 1$.** Då gäller $U_L'(1) \ge 0$ och $U_B'(1) \le 0$. Nyttan ökar fram till $y = 1$ och minskar efter, så toppen ligger i knäcken.
- **$y^* = 1$ ⇒ $A$ i intervallet.** Om $A$ låg utanför skulle en av derivatorna i $y = 1$ peka bort från knäcken. Då kunde man öka nyttan genom att flytta $y$, och $y = 1$ vore inte optimalt.

Tre saker att hålla isär:

1. **Ändpunkterna ingår.** Vid $A = 4.0230$ är $y_L = 1$, och vid $A = 1.5343$ är $y_B = 1$. Där sammanfaller den vanliga lösningen med knäcken.
2. **Det gäller optimalt $y$.** Vem som helst *kan* välja $y = 1$. Intervallet säger för vilka $A$ det är det *bästa* valet.
3. **$P^*$ är fast.** Gränserna räknas med $E_P$ och $\sigma_P^2$ för tangentportföljen från (b).

**Erik ($A_X = 0$).** Hans nytta är definierad för varje $y$, men den saknar maximum. Med $A = 0$ försvinner variansstraffet, och nyttan blir bara förväntad avkastning:

$$
U(1) = E_P = 0.0785, \qquad U_B'(y) = E_P - r_B = 0.0185 > 0 \quad\text{för alla } y > 1
$$

- $U(1)$ är ett giltigt tal. Problemet är inte att nyttan saknas.
- $y = 1$ är inte optimalt för honom, eftersom varje extra lånad krona höjer nyttan med 1.85 %. Nyttan växer utan gräns, så $y^* = \infty$.
- Det stämmer med intervallet: $A = 0 < 1.5343$.

Mäter man i stället Eriks riskaversion med Bet Z blir $A_Z = 2(0.07 - 0.05)/0.16^2 = 1.5625$. Det ligger precis inne i intervallet, och då hade han hållit exakt $P^*$.

## 6. Varför två regioner, och varför det inte är ett cirkelargument

**Regionerna gäller valen, inte investerarna.** Varje investerare kan välja vilket $y$ som helst, och för varje $y$ är räntan redan bestämd:

- $y = 0.7$: 0.3 lånas ut till 3 %.
- $y = 1.3$: 0.3 lånas till 6 %.

$U(y)$ är alltså en helt känd funktion innan man optimerar. Räntan $r(y)$ är inte en okänd parameter. Den är en del av funktionen, på samma sätt som skattesatsen i ett progressivt skatteschema beror på inkomsten utan att schemat blir cirkulärt.

**Varför det kan se cirkulärt ut.** Det kan verka som att man behöver $r$ för att räkna ut $y$, och $y$ för att veta $r$. Men $y_L$ och $y_B$ är bara *kandidater*. Man räknar ut båda och kontrollerar sedan om var och en hamnar på sin egen sida:

| Kandidat | Giltig om |
|---|---|
| $y_L = \dfrac{E_P - r_f}{A\sigma_P^2}$ | $y_L \le 1$ |
| $y_B = \dfrac{E_P - r_B}{A\sigma_P^2}$ | $y_B \ge 1$ |

Det är "gissa och verifiera", och svaret är entydigt eftersom $U$ är konkav.

**Det tredje utfallet.** Ta Elaine med $A = 3$:

- Om hon lånar ut till 3 % vill hon ha $y_L = 1.341$. Men det betyder att hon lånar, så räntan är inte längre 3 %.
- Om hon lånar till 6 % vill hon ha $y_B = 0.511$. Men då lånar hon ju inte, hon lånar ut.

Båda kandidaterna pekar mot den andra sidan. Hon vill öka $y$ så länge det är billigt, men inte när det blir dyrt, och därför stannar hon exakt på $y = 1$. Det gäller för ett helt intervall av $A$, inte bara ett enstaka värde.

**$y^*$ är en funktion av $A$, i tre delar:**

$$
y^*(A) = \begin{cases}
\dfrac{E_P - r_B}{A\sigma_P^2} > 1, & A < 1.5343 \quad\text{(lånar)}\\[8pt]
1, & 1.5343 \le A \le 4.0230 \quad\text{(knäcken)}\\[8pt]
\dfrac{E_P - r_f}{A\sigma_P^2} < 1, & A > 4.0230 \quad\text{(lånar ut)}
\end{cases}
$$

Varje investerare hamnar alltså på ett enda ställe, och man ser direkt på $A$ var. Men gränserna 1.5343 och 4.0230 kommer från att man jämfört båda grenarna i $y = 1$. Därför behövs båda regionerna i härledningen.

![y*(A) med platt del vid y = 1](/repo/web/content/knackt-cal/y_of_A.png)

Den svarta kurvan är $y^*(A)$. Den följer den blå prickade $y_L$ för stora $A$ och den gröna streckade $y_B$ för små $A$. Däremellan hoppar den inte mellan kurvorna, utan ligger platt på $y = 1$. Utan knäck, det vill säga om $r_B = r_f$, vore $y^*$ hela den blå kurvan, och bara $A = 4.0230$ skulle ge exakt $y = 1$.

## 7. Samma sak i $(\sigma, E)$-planet

CAL består av två räta linjer som möts i $P^*$:

$$
E = \begin{cases}
r_f + \dfrac{E_P - r_f}{\sigma_P}\,\sigma, & \sigma \le \sigma_P \quad (\text{lutning } 0.4417)\\[8pt]
r_B + \dfrac{E_P - r_B}{\sigma_P}\,\sigma, & \sigma > \sigma_P \quad (\text{lutning } 0.1684)
\end{cases}
$$

Indifferenskurvorna är $E = U + \tfrac12 A\sigma^2$. Den bästa punkten är där den högsta indifferenskurvan nuddar CAL.

- Till vänster om $P^*$ tangerar kurvan den branta delen (fall 1).
- Till höger om $P^*$ tangerar den den flacka delen (fall 2).
- Om kurvans lutning $A\sigma_P$ i $P^*$ ligger mellan 0.1684 och 0.4417, ligger kurvan i hörnet (fall 3).

Det sista villkoret är samma intervall som i avsnitt 5, multiplicerat med $\sigma_P$.

![Knäckt CAL med indifferenskurvor](/repo/web/content/knackt-cal/cal.png)

## 8. Exempel

| $A$ | $y_L$ | $y_B$ | Fall | $y^*$ | $1 - y^*$ | $U^*$ |
|---|---|---|---|---|---|---|
| 6.0 | 0.6705 | 0.2557 | 1, lånar ut | 0.6705 | 0.3295 | 0.04626 |
| 3.0 (Elaine) | 1.3410 | 0.5114 | 3, knäcken | 1 | 0 | 0.06041 |
| 1.2 | 3.3525 | 1.2786 | 2, lånar | 1.2786 | $-0.2786$ | 0.07182 |

Med $A = 1.5$ (Chen) gäller $y_B = 1.0228 \ge 1$, så Chen lånar, men bara lite. Det stämmer med att $1.5 < 1.5343$.

## 9. Förbehåll: $P^*$ är fast här

Allt ovan håller $P^*$ fast, det vill säga tangentportföljen räknad med $r_f$. Om man lånar och får välja mixen fritt, är den relevanta tangentportföljen den som räknas med $r_B$, alltså $\Sigma^{-1}(\boldsymbol\mu - r_B\mathbf 1)$. Den har en annan mix. Det är poängen i (d), som finns på `FINA 3103/html/borrowing.html`.

```python
y_L = (E_P - r_f) / (A * var_P)
y_B = (E_P - r_B) / (A * var_P)
y = y_L if y_L <= 1 else (y_B if y_B >= 1 else 1.0)
```
