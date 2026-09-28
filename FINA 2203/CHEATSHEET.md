# FINA 2203 – Cheat sheet, Fundamentals of Business Finance

Källa: Berk & DeMarzo, *Corporate Finance*, 6th Global Edition (`HKUST books/Corporate Finance.pdf`). Sidhänvisningar "(s. N)" avser bokens sidnumrering. Kapitel 3–7 täcks av assignment 1–3; kapitel 8–9 är kommande. Facitsiffror från assignments står i tabeller så att egna beräkningar kan verifieras.

## 0. Notation

| Symbol | Betydelse |
|---|---|
| `r` | diskonteringsränta / cost of capital per period, i decimalform |
| `C`, `C_t` | kassaflöde, kassaflöde vid tidpunkt `t` |
| `N`, `n` | antal perioder |
| `PV`, `FV` | present value, future value |
| `g` | tillväxttakt per period |
| `APR`, `EAR` | annual percentage rate (nominell), effective annual rate |
| `m`, `k` | antal ränteperioder per år |
| `IRR` | internal rate of return |
| `NPV` | net present value |
| `a_n` | nuvärdesfaktor för annuitet, `(1 − (1+r)^(−n))/r` |

## 1. Grundprinciper (kap. 3, s. 99–135)

**Valuation principle** (s. 100–105): värdet av ett beslut är marknadsvärdet av dess nyttor minus marknadsvärdet av dess kostnader, allt omräknat till samma tidpunkt med marknadspriser.

**NPV-regeln** (s. 106–109): ta projekt med `NPV > 0`; välj det med högst NPV bland alternativ. NPV är projektets värde i dagens kronor och oberoende av investerarens preferenser.

$$ NPV = PV(\text{inflöden}) - PV(\text{utflöden}) = \sum_{t=0}^{N} \frac{C_t}{(1+r)^t} $$

**Law of One Price** (s. 110–115): två tillgångar med identiska kassaflöden har samma pris, annars finns arbitrage. Pris på en säkerhet = PV av dess kassaflöden. Vid ett konkurrensutsatt marknadspris är NPV av att köpa eller sälja noll.

**Risk** (s. 116–120): riskfyllda kassaflöden diskonteras med `r_f + riskpremie`. Riskpremien beror på korrelation med marknaden, inte på volatiliteten i sig.

## 2. Tidsvärde (kap. 4, s. 136–180)

### Tre regler för tidsresor (s. 138–143)

1. Bara kassaflöden vid **samma tidpunkt** får jämföras eller adderas.
2. Flytta framåt: `FV_n = C·(1+r)^n` (compounding).
3. Flytta bakåt: `PV = C/(1+r)^n` (discounting).

### Ström av kassaflöden (s. 144–148)

$$ PV = \sum_{t=0}^{N} \frac{C_t}{(1+r)^t}, \qquad FV_N = PV\,(1+r)^N $$

### Perpetuitet (s. 149–151)

Första betalningen om **en period**:

$$ PV(\text{perpetuitet}) = \frac{C}{r} $$

Med tillväxt `g < r` (s. 156–158):

$$ PV = \frac{C}{r - g} $$

`C` är första betalningen (vid `t = 1`), inte dagens värde.

### Annuitet (s. 151–155)

`N` lika betalningar `C`, första om en period:

$$ PV = C \cdot \frac{1}{r}\left(1 - \frac{1}{(1+r)^N}\right) = C\,a_N, \qquad FV_N = C \cdot \frac{1}{r}\left((1+r)^N - 1\right) $$

Med tillväxt `g` (s. 158–160):

$$ PV = C \cdot \frac{1}{r-g}\left(1 - \left(\frac{1+g}{1+r}\right)^N\right) $$

**Lösa ut betalningen** (s. 163–165), t.ex. lånebetalning:

$$ C = \frac{PV}{a_N} = \frac{PV}{\frac{1}{r}\left(1 - (1+r)^{-N}\right)} $$

**Lösa ut antal perioder** (s. 165) med logaritmer, t.ex. sparande: `N = ln(FV·r/C + 1)/ln(1+r)`.

### Tidsförskjutna flöden, vanliga fällor

- Perpetuitet/annuitet vars första betalning kommer vid `t = k` i stället för `t = 1`: värdera med formeln vid `t = k − 1` och diskontera `k − 1` perioder. `C/r` är alltså värdet **en period före** första betalningen.
- Annuitet med första betalning **idag** (annuity due): `PV = C + C·a_{N−1}` eller `C·a_N·(1+r)`.
- Årliga formler kräver att `r` och `N` är i samma periodenhet som `C` (månad, kvartal, år). Konvertera räntan först (avsnitt 3).

### IRR (s. 166–169)

Den ränta som ger `NPV = 0`. Sluten lösning bara i specialfall: två flöden `IRR = (FV/P)^(1/N) − 1`; perpetuitet `IRR = C/P`; växande perpetuitet `IRR = C/P + g`. Annars numeriskt (`scipy.optimize.brentq`, Excel `IRR`).

## 3. Räntor (kap. 5, s. 181–208)

### EAR och APR (s. 182–186)

EAR är den effektiva årsräntan, APR den nominella med `k` kapitaliseringar per år.

$$ 1 + EAR = \left(1 + \frac{APR}{k}\right)^{k}, \qquad \text{ränta per period} = \frac{APR}{k} $$

Konvertera en effektiv ränta till en annan periodlängd:

$$ \text{ränta över } n \text{ perioder} = (1 + r)^{n} - 1 $$

t.ex. månadsränta ur EAR: `(1+EAR)^(1/12) − 1`. **APR utan angiven kapitalisering betyder ingenting**; APR är inte en diskonteringsränta förrän den delats med `k`.

### Lån (s. 186–187)

Amorterande lån: betalningen `C` löser `L = C·a_N` med periodräntan `APR/k`. Restskuld vid tidpunkt `t` = PV av återstående betalningar = `C·a_{N−t}`. Räntedelen av en betalning = restskuld × periodränta.

### Realränta (s. 187–189)

$$ 1 + r_{real} = \frac{1 + r_{nom}}{1 + i} \quad\Rightarrow\quad r_{real} \approx r_{nom} - i $$

### Avkastningskurva och riskfri ränta (s. 189–194)

Kassaflöde vid `t` diskonteras med spoträntan `r_t` för just den löptiden: `PV = Σ C_t/(1+r_t)^t`. En brant kurva signalerar förväntade räntehöjningar.

### Skatt (s. 195–197)

$$ r_{\text{efter skatt}} = r\,(1 - \tau) $$

Räntekostnader på lån är ofta avdragsgilla; jämför alltid räntor på samma skattebasis.

### Opportunity cost of capital (s. 198–200)

Diskonteringsräntan för ett projekt är den bästa förväntade avkastningen på en alternativ investering **med samma risk och löptid**, inte företagets låneränta.

## 4. Obligationer (kap. 6, s. 209–247)

### Nollkupong (s. 210–212)

$$ P = \frac{FV}{(1 + YTM_n)^n}, \qquad YTM_n = \left(\frac{FV}{P}\right)^{1/n} - 1 $$

Riskfri spotränta `r_n = YTM_n` för statspapper.

### Kupongobligation (s. 212–215)

Kupong `CPN = kupongränta · FV / antal kuponger per år`. Med `y` = YTM per kupongperiod och `N` kuponger kvar:

$$ P = CPN \cdot \frac{1}{y}\left(1 - \frac{1}{(1+y)^N}\right) + \frac{FV}{(1+y)^N} $$

YTM anges som APR med samma kapitalisering som kupongerna. Löses numeriskt ur prisekvationen.

### Pris, kupong och yield (s. 215–221)

| Villkor | Pris |
|---|---|
| kupongränta > YTM | över par (premium) |
| kupongränta = YTM | par |
| kupongränta < YTM | under par (discount) |

Pris och ränta rör sig i motsatt riktning. Längre löptid och lägre kupong ger högre räntekänslighet. Mellan kupongdatum stiger priset med upplupen ränta och faller vid kupongutbetalning. Vid konstant YTM konvergerar priset mot par.

### Replikering och arbitrage (s. 221–224)

En kupongobligation = portfölj av nollkuponger: `P = Σ CPN/(1+r_t)^t + FV/(1+r_N)^N`. Avviker marknadspriset finns arbitrage. YTM på en kupongobligation är ett viktat medel av spoträntorna.

### Företagsobligationer (s. 224–228)

YTM är den **utlovade** avkastningen, förväntad avkastning är lägre vid default-risk. Credit spread = YTM − riskfri ränta för samma löptid.

## 5. Investeringsbeslut (kap. 7, s. 248–274)

### NPV-regeln (s. 249–252)

Ta projektet om `NPV > 0` vid cost of capital `r`. NPV-profilen `NPV(r)` visar känsligheten; skärningen med x-axeln är IRR. Skillnaden `IRR − r` är den maximala felmarginalen i uppskattningen av `r` innan beslutet ändras.

### IRR-regeln (s. 252–256)

Ta projektet om `IRR > r`. Ger samma svar som NPV **bara** när alla negativa flöden kommer före alla positiva. Regeln fallerar när:

- kassaflödet **byter tecken flera gånger** (t.ex. investering, inflöden, städkostnad): flera IRR eller ingen,
- projektet är en **finansiering** (positivt flöde först): då ska IRR vara *lägre* än `r`,
- projekt av **olika storlek eller löptid** jämförs: IRR mäter procent, inte värde.

### Payback (s. 256–258)

Antal år till att ackumulerade odiskonterade flöden ≥ investeringen. Lika flöden: `payback = investering / årligt flöde`; olika flöden: ackumulera och interpolera i brytåret. Ignorerar tidsvärde och alla flöden efter brytpunkten, så regeln kan förkasta projekt med positivt NPV.

### Välja mellan projekt (s. 258–265)

Ömsesidigt uteslutande projekt: **högst NPV**, inte högst IRR. Incremental IRR = IRR på skillnaden i kassaflöden mellan två projekt; kräver samma teckenmönster och samma risk för att vara meningsfull.

### Resursbegränsning (s. 265–268)

Profitability index:

$$ PI = \frac{NPV}{\text{förbrukad resurs}} $$

Ranka efter PI och ta projekt tills resursen är slut. Fungerar bara om resursen används fullt ut och det finns en enda begränsning.

## 6. Kapitalbudgetering (kap. 8, s. 275–312, kommande)

### Från resultat till fritt kassaflöde (s. 276–288)

$$ \text{Unlevered net income} = (\text{Revenues} - \text{Costs} - \text{Depreciation}) \times (1 - \tau_c) $$

$$ FCF_t = \text{Unlevered NI}_t + \text{Depreciation}_t - CapEx_t - \Delta NWC_t $$

där `NWC = Cash + Inventory + Receivables − Payables` och `ΔNWC_t = NWC_t − NWC_{t−1}`. Avskrivningar är inte kassaflöden men ger skatteskölden `Depreciation · τ_c`.

**Principer:** räkna bara **inkrementella** flöden. Ta med opportunity costs, externaliteter (kannibalisering) och sunk costs **exkluderas**. Räntekostnader exkluderas i unlevered FCF, de fångas i `r`.

### NPV och justeringar (s. 288–295)

`NPV = Σ FCF_t/(1+r)^t`. Vid försäljning av tillgång: `after-tax salvage = salvage − τ_c·(salvage − book value)`. Terminal value för fortsatt verksamhet: växande perpetuitet på sista årets FCF.

### Känslighet (s. 295–300)

Break-even: värdet på en parameter som ger `NPV = 0`. Sensitivity analysis: NPV vid bästa/sämsta utfall per parameter. Scenario analysis: flera parametrar samtidigt.

## 7. Aktievärdering (kap. 9, s. 313–349, kommande)

### Dividend-discount model (s. 314–323)

$$ P_0 = \frac{Div_1 + P_1}{1 + r_E}, \qquad r_E = \underbrace{\frac{Div_1}{P_0}}_{\text{dividend yield}} + \underbrace{\frac{P_1 - P_0}{P_0}}_{\text{capital gain rate}} $$

Konstant tillväxt (Gordon):

$$ P_0 = \frac{Div_1}{r_E - g}, \qquad g = \text{retention rate} \times \text{return on new investment} $$

Utdelning: `Div_t = EPS_t × payout ratio`. Att sänka utdelningen för att investera höjer priset bara om avkastningen på investeringen överstiger `r_E`.

### Total payout och FCF-modell (s. 323–330)

$$ P_0 = \frac{PV(\text{framtida utdelningar och återköp})}{\text{antal aktier}}, \qquad V_0 = PV(FCF) , \quad P_0 = \frac{V_0 + Cash_0 - Debt_0}{\text{antal aktier}} $$

FCF diskonteras med WACC, utdelningar med `r_E`.

### Multiplar (s. 330–334)

`P/E = P_0/EPS_1 = payout/(r_E − g)` för en Gordon-aktie. Enterprise value multiplar `EV/EBITDA`, `EV/Sales`. Jämförbara företag måste ha likartad risk, tillväxt och kapitalstruktur.

## 8. Facit från assignments

| Uppgift | Indata | Facit |
|---|---|---|
| FastTrack Bikes (P 8-11a), NPV | `C = 211 400` år 1–6, `CF = 304 300` år 7–16, `r = 9.2 %` | `NPV = 198 944` ⇒ investera |
| FastTrack (P 8-11c), utvecklingstid | NPV = 0 ⇒ `v^n = (C/r)/(C/r + CF·a_10)` | `n = 6.94` år |
| Kolgruva (P 8-x), NPV | `−118.7`, `+20.8` år 1–10, `−1.9` perpetuitet från år 11, `r = 7.9 %` | `NPV = 10.258` ⇒ acceptera; IRR-regeln ej användbar (två IRR) |
| Utrustning (P 8-23) | `1.04` per år i 7 år, `r = 12.1 %` | max pris `4.73` |
| Payback (P 8-26) | `548 000`, `121 000` per år i 10 år, `r = 10.6 %` | payback `4.53` år > 3; `NPV ≈ 176 000 > 0` ⇒ ta projektet |

## 9. Python-mönster

```python
import math
from scipy.optimize import brentq

def pv_annuity(C, r, n):            # first payment at t = 1
    return C / r * (1 - (1 + r) ** -n)

def pv_perpetuity(C, r, g=0.0, first=1):   # first payment at t = first
    return C / (r - g) / (1 + r) ** (first - 1)

def npv(rate, cfs):                 # cfs = {t: cash flow}
    return sum(cf / (1 + rate) ** t for t, cf in cfs.items())

def irr(cfs, lo=-0.99, hi=1.0):
    return brentq(lambda r: npv(r, cfs), lo, hi)

def ear_from_apr(apr, k):  return (1 + apr / k) ** k - 1
def period_rate(ear, k):   return (1 + ear) ** (1 / k) - 1
```

## 10. Vanliga fel

- **(a) Globala variabler i funktioner.** Skriv `rate` i kroppen om parametern heter `rate`; annars hämtas ett gammalt `r` från en annan cell utan felmeddelande. Starta om kerneln och kör cellen ensam för att avslöja det.
- **(b) Perpetuitet som börjar sent.** `C/r` är värdet en period före första betalningen. Första betalning vid år 11 ⇒ diskontera 10 år, inte 11.
- **(c) Tecken på kostnader.** Städ- och underhållskostnader är utflöden och ska subtraheras.
- **(d) Antal perioder.** "Development takes 6 years" ⇒ `range(1, 7)`, inte `range(1, 6)`. Kontrollera alltid längden på det du summerar.
- **(e) "Round to two decimals" på ett antal år** ⇒ lös `NPV(n) = 0` kontinuerligt med logaritmer, inte heltalssökning.
- **(f) APR ≠ diskonteringsränta.** Dela med `k` för periodräntan, eller konvertera till EAR först.
- **(g) IRR-regeln** gäller bara med ett teckenbyte. Vid flera teckenbyten eller när projekt jämförs: använd NPV.
- **(h) Payback** säger inget om värde. Frågan "should you take the project to increase value" besvaras alltid med NPV.
