# MATH 4511 – Cheat sheet, Lecture Note 1 (Introduction to interest rate derivatives, Part 1)

Sidhänvisningar "(s. N)" avser `pdf/MATH4511_L1.pdf`. Facitsiffror från föreläsningens exempel står i tabeller så att egna beräkningar kan verifieras.

## 0. Notation

| Symbol | Betydelse |
|---|---|
| `F` | face value / par; `C = F` för straight-term bond (s. 4) |
| `c`, `r = c/m` | årlig nominell kupongränta resp. kupongränta per period; kupong = `rF` (s. 5) |
| `N = nT` | löptid i år, `n` kuponger, `T` år per kupongperiod (s. 5) |
| `j`, `i^(m) = mj`, `i` | effektiv yield per period, annual nominal yield (YTM), annual effective yield (s. 7–8) |
| `B(t;T)` | pris vid `t` av zero-coupon bond som betalar 1 vid `T` (s. 18) |
| `s_0(t)` | spot rate för `t` år, annual effective (s. 19) |
| `R_[T1,T2]` | effektiv ränta över perioden `[T1,T2]` (ej annualiserad) (s. 42–43) |
| `L_[T1,T2]` | kvoterad årsränta (LIBOR/spot) för samma period (s. 43, 53) |
| `K_[T1,T2]`, `f_[T1,T2]` | forward rate över `[T1,T2]` som periodränta resp. annualiserad (s. 75) |
| `X` (ibland `K`) | delivery price i forwardkontrakt; `f_t` = kontraktets värde vid `t` (s. 62, 64) |

## 1. Räntekonventioner

### Omräkning mellan konventioner (s. 7–8, 21, 64)

| Konvention | Kvot | Tillväxt av 1 under `t` år | `B(0;t)` |
|---|---|---|---|
| Annual effective | `i` | `(1+i)^t` | `(1+i)^(-t)` |
| Nominell, `m` perioder/år | `i^(m)` | `(1+i^(m)/m)^(mt)` | `(1+i^(m)/m)^(-mt)` |
| Kontinuerlig (`m = ∞`) | `r` | `e^(rt)` | `e^(-rt)` |

$$ i = (1+j)^m - 1 = \Bigl(1+\tfrac{i^{(m)}}{m}\Bigr)^m - 1, \qquad j = \tfrac{i^{(m)}}{m} \quad (\text{s. } 8) $$

- `m = 2` = semi annual bond basis (SABB), USA-marknaden; `m = ∞` vanligt i finansiell litteratur (s. 21).
- Spot rate från zero-coupon-pris (s. 18–19): `B(0;t) = 1/(1+s_0(t))^t  ⇔  s_0(t) = B(0;t)^(-1/t) − 1`.
- Kontinuerlig spot `L`: `B(0;T) = e^(−L·T)` (s. 64, 76).

### Periodränta kontra kvoterad årsränta

$$ R_{[t,T]} = \frac{1}{B(t;T)} - 1 \qquad\Longleftrightarrow\qquad B(t;T) = \frac{1}{1+R_{[t,T]}} \quad (\text{s. } 54\text{–}55) $$

| Kvotering av `L` för period av längd `τ = T − t` år | `R_[t,T]` |
|---|---|
| Annual effective (t.ex. Ex 7, s. 43 med `τ = 0.5`) | `(1+L)^τ − 1` |
| LIBOR-konvention: nominell, enkel ränta, `m = 1/τ` (Ex 10, s. 53) | `L/m = L·τ` |
| Kontinuerlig | `e^(Lτ) − 1` |

**LIBOR-regeln:** kupong på FRN = `F · L/m` (s. 53: `1000 × 0.028/2 = 14`). Kontrollera alltid vilken konvention uppgiften anger; Ex 7 (s. 42) säger uttryckligen "quoted as annual effective" och använder då `R = (1+L)^(1/2) − 1`.

### Termstruktur (s. 17–24)

- `{s_0(t)}_{t>0}` = term structure. Normal (stigande), inverted (fallande), flat (`s_0(t) ≡ c`) (s. 20).
- Teorier: liquidity theory, expectation theory (`R_[1,2]` slumpmässig), market segmentation (s. 22–24).

## 2. Obligationsprissättning

### Fixed rate coupon bond, yield-metoden (s. 9–10)

$$ P_0 = \sum_{k=1}^{n}\frac{rF}{(1+j)^k} + \frac{F}{(1+j)^n} = rF\,\frac{1-(1+j)^{-n}}{j} + F(1+j)^{-n} \quad (\text{s. } 9) $$

$$ P_0(i) = \sum_{k=1}^{n}\frac{rF}{(1+i)^{kT}} + \frac{F}{(1+i)^{nT}} \quad (i \text{ annual effective, s. } 10) $$

Yield beror på pris: högt pris ⇔ låg yield (s. 10). YTM = `i^(m) = mj` löses numeriskt ur prisekvationen (Ex 2, s. 13).

| Exempel | Indata | Facit |
|---|---|---|
| Ex 1a (s. 11) | `F=100, c=6 % kvartalsvis, i^(4)=6.2 %, 6 år` | `P_0 = 99.00427` |
| Ex 1b (s. 12) | yield → 5.6 % efter 2 år, 16 kuponger kvar | `P_2 = 101.4246` |
| Ex 2 (s. 13) | `F=1500, c=8 % kvartalsvis, 5 år, pris 1602` | `j ≈ 0.016`, `i^(4)=0.064`, `i = 0.065552` |

### Pris mellan kupongdatum: dirty vs clean (s. 14–16)

Låt `t = (k+f)T`, `0 < f < 1`, `i` annual effective vid `t`:

$$ P(t) = \sum_{j=k+1}^{n}\frac{rF}{(1+i)^{jT-t}} + \frac{F}{(1+i)^{nT-t}} \quad (\text{dirty price, s. } 14) $$

- Accrued interest (till säljaren) = `f · rF` (s. 15).
- **Clean price = `P(t) − f·rF`** (s. 16). Köparen betalar dirty price och får hela nästa kupong.

### Prissättning med spot rates (s. 25) och replikering (s. 50)

$$ P_0 = \sum_{k=1}^{n}\frac{rF}{(1+s_0(kT))^{kT}} + \frac{F}{(1+s_0(nT))^{nT}} = \sum_{k=1}^{n} rF\,B(0;kT) + F\,B(0;nT) $$

Replikerande portfölj (Ex 8, s. 50): köp zero-coupon bonds med face `rF` vid `T, …, (n−1)T` och face `F + rF` vid `nT`; law of one price ger formeln.

| Exempel | Indata | Facit |
|---|---|---|
| Ex 4a (s. 26) | `F=500, c=4 % årligen, 4 år; spot 3 / 3.5 / 3.8 / 4 %` | `P_0 = 500.4688` |
| Ex 4b (s. 26) | alla spot −0.25 % efter 1 år; 3 flöden kvar, spot 2.75 / 3.25 / 3.55 % | `P_1 = 506.5566` |

### Bootstrapping av spot rates

Föreläsningen ger spot rates direkt eller via zero-coupon-priser (Ex 9, s. 51: `s_0(1) = 1/B(0;1) − 1 = 0.022`). Vid bootstrapping från kupongobligationer löses `B(0;nT)` rekursivt ur `P_0 = Σ rF B(0;kT) + F B(0;nT)` med redan kända `B(0;kT)`, `k < n`, och sedan `s_0(nT) = B(0;nT)^(−1/(nT)) − 1`.

### No arbitrage-principen (s. 44–46)

Arbitrage: (1) självfinansierande, (2) payoff ≥ 0 med sannolikhet 1, (3) positiv payoff med positiv sannolikhet. Rule 1 (law of one price): identiska payoffs ⇒ samma pris. Rule 2: dominerande payoff ⇒ högre pris (s. 45).

## 3. Duration och konvexitet

### Definitioner för en tillgång med flöden `C_k` vid `t_k`, `i` annual effective (s. 27–28, 33)

$$ D_{Mod}(i) = -\frac{P'(i)}{P(i)} = \frac{1}{1+i}\,D_{Mac}(i), \qquad D_{Mac}(i) = \frac{\sum_k t_k\,C_k(1+i)^{-t_k}}{\sum_k C_k(1+i)^{-t_k}} $$

$$ C_{Mod}(i) = \frac{P''(i)}{P(i)} = \frac{\sum_k t_k(t_k+1)\,C_k(1+i)^{-t_k-2}}{P(i)} = \frac{\sum_k t_k(t_k+1)\,PV(C_k)}{(1+i)^2 P(i)} \quad (\text{s. } 33) $$

Andra konventioner (s. 29): nominell `m`-thly yield ⇒ `D_Mod = D_Mac/(1+i/m)` med `PV` beräknad som `C_k(1+i/m)^(−m t_k)`; kontinuerlig ⇒ `D_Mod = D_Mac`.

**Samband att komma ihåg:** `D_Mac = (1+i)·D_Mod` (annual effective).

### Approximationer (s. 30, 34, 36)

$$ \frac{P(i_0+\varepsilon)-P(i_0)}{P(i_0)} \approx -\varepsilon D_{Mod} \quad (\text{1:a ordn.}), \qquad \approx -\varepsilon D_{Mod} + \frac{\varepsilon^2}{2}C_{Mod} \quad (\text{2:a ordn.}) $$

$$ P(i_0+\varepsilon) \approx P(i_0)\Bigl[1 - \varepsilon D_{Mod} + \tfrac{\varepsilon^2}{2}C_{Mod}\Bigr] \quad (\text{s. } 36) $$

| Exempel | Indata | Facit |
|---|---|---|
| Ex 5 (s. 31–32) | `F=1500, c=6.8 % kvartalsvis, 12 år, i^(4)=7.4 %` | `D_Mac = 8.19332641`, `D_Mod = 8.19332641/1.0185 = 8.0445031`; `ΔP/P ≈ −0.01609` (exakt `−0.01592`), `P(0.074)=1428.831`, `P(0.076)=1406.08` |
| Ex 6 (s. 35–37) | `F=1000, c=5 % årligen, 10 år, i_0=5 %` | `P=1000`, `D_Mod = 7.721735`, `C_Mod = 74.99768` |
| Ex 6a, `ε = 0.0025` | | 1:a `980.6957`, 2:a `980.93`, exakt `980.9279` |
| Ex 6b, `ε = 0.025` | | 1:a `806.9566`, 2:a `830.3934`, exakt `828.398` |

### Portfölj (s. 38–41)

Gemensam yield `i` (s. 39) och parallellskift `ε` av olika yields `i_1, …, i_n` (s. 40–41) ger samma resultat: viktat medelvärde med vikter `P_k/P`.

$$ D_{Mod} = \sum_{k=1}^{n}\frac{P_k}{P}\,D^{k}_{Mod}, \qquad C_{Mod} = \sum_{k=1}^{n}\frac{P_k}{P}\,C^{k}_{Mod} $$

(Obs: på s. 40 står `C_Mod(i⃗) = −P''(ε)/P(ε)|_{ε=0}` med minustecken; s. 41 och s. 33 har plus, vilket är det korrekta.)

## 4. Floating rate note (FRN)

### Kupongregel (s. 42–43)

Kupong vid `T_i` = `F · R_[T_{i−1},T_i]`, där räntan sätts ("fixas") vid `T_{i−1}` och betalas vid `T_i`. Nästa kupong är därför alltid känd.

| Ex 7 (s. 42–43): `F=1000`, 6-mån LIBOR annual effective | 0 | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 |
|---|---|---|---|---|---|---|---|
| `L` (kvoterad vid tidpunkten) | 2 % | 2.1 % | 1.7 % | 1.9 % | 2 % | 2.2 % | 2.4 % |
| Kupong betald vid nästa datum, `1000((1+L)^0.5 − 1)` | – | 9.95 | 10.45 | 8.46 | 9.46 | 9.95 | 10.94 |

### Pris (s. 47–49, 54)

- Replikering av kupong `i`: köp `T_{i−1}`-bond face `F`, short `T_i`-bond face `F`, återinvestera ⇒ `F R_[T_{i−1},T_i]` vid `T_i` (s. 47).
- `V_0 = Σ [F B(0;T_{i−1}) − F B(0;T_i)] + F B(0;T_n) = F` — **par vid emission och vid varje kupongdatum** (s. 48–49).
- Mellan kupongdatum, `T_k < t < T_{k+1}` (s. 49, 54):

$$ V_t = \bigl(F\,R_{[T_k,T_{k+1}]} + F\bigr)\,B(t;T_{k+1}) = F\bigl(1+R_{[T_k,T_{k+1}]}\bigr)\frac{1}{1+R_{[t,T_{k+1}]}} $$

| Exempel | Indata | Facit |
|---|---|---|
| Ex 9a (s. 51–52) | `F=1000`, kupong = 1-års spot + 30 bp årligen, `B(0;1)=0.978474` | `L_[0,1] = 0.022`, kupong 1 = `1000(0.022+0.003) = 25` |
| Ex 9b | `B(0;2)=0.951814, B(0;3)=0.920493` | `V_0 = 1000 + 3(B(0;1)+B(0;2)+B(0;3)) = 1008.5523` |
| Ex 10 (s. 53–54) | `F=1000`, 6-mån LIBOR 2.8 % nominell semi; efter 3 mån 3-mån LIBOR 2.65 % | kupong `= 14`; `V_0.25 = 1014/(1+0.0265/2)^(1/2) = 1007.348` |

### Duration av FRN (s. 55–56)

- På kupongdatum: `V_t = F`, `dV_t/dL = 0` ⇒ `D_Mod = D_Mac = 0`.
- Mellan datum (`T_{k−1} < t < T_k`), derivera m.a.p. `L_[t,T_k]`:

$$ D_{Mod} = \frac{T_k - t}{1+L_{[t,T_k]}}, \qquad D_{Mac} = T_k - t \;=\; \text{tid till nästa kupong} $$

### Fast vs flytande, Example 10 (s. 57–59)

Flat term structure 2.5 % annual effective. Bond A: 3-års fixed, `c = 2.5 %` årligen (pris = par). Bond B: 3-års FRN, kupong = 1-års LIBOR årligen.

| Vid `t = 0`, spot | 2.25 % | 2.5 % | 2.75 % |
|---|---|---|---|
| Bond A (fixed) | 1007.175 | 1000 | 992.8943 |
| Bond B (floating) | 1000 | 1000 | 1000 |

| Vid `t = 0.5` (LIBOR 2.5 % vid `t=0`, första kupong 25 låst), spot | 2.25 % | 2.5 % | 2.75 % |
|---|---|---|---|
| Bond A (fixed) | 1018.442 | 1012.423 | 1006.454 |
| Bond B (floating) `= 1025·B(0.5;1)` | 1013.66 | 1012.423 | 1011.19 |

`D^A_Mac(i_0.25) = [0.5·25/1.025^0.5 + 1.5·25/1.025^1.5 + 2.5·1025/1.025^2.5]/1012.423 ≈ 2.427424` år, `D^B_Mac = 0.5` år (s. 59). FRN har kortare duration ⇒ mindre räntekänslig.

## 5. Forwardkontrakt

### Tillgång utan utdelning (s. 60–64)

Portfolio 1 = long forward + `T`-års zero-coupon bond med face `X`; Portfolio 2 = 1 enhet av tillgången. Båda ger 1 enhet vid `T` ⇒ samma värde vid varje `t < T` (s. 61–62):

$$ f_0 + X\,B(0;T) = S_0 \;\Rightarrow\; f_0 = S_0 - X\,B(0;T); \qquad f_0 = 0 \;\Rightarrow\; X = \frac{S_0}{B(0;T)} \quad (\text{s. } 62) $$

$$ f_t = S_t - X\,B(t;T) \quad (\text{pågående kontrakt, lång position, s. } 64) $$

Om `X > S_0/B(0;T)` lånar köparen `S_0` och köper direkt; om `X <` säljer säljaren nu och köper bond (s. 63).

| Ex 11 (s. 64) | `S_0 = 50`, 2-års kontinuerlig spot 2 % | `X = 50e^(0.04) = 52.04054` |
|---|---|---|
| efter 1 år, 1-års spot 1.9 % kont. | `S_1 = 55` / `S_1 = 47` | `f_1 = 55 − 52.04054e^(−0.019) = 3.9389` / `−4.0611` |

### Forward på kupongobligation, Example 12 (s. 65–67)

Kuponger `rF` vid `T_C, 2T_C, …`; `k` kuponger faller inom `[0,T]` och tillfaller säljaren ⇒ dras bort:

$$ X = \frac{S_0 - \sum_{i=1}^{k} rF\,B(0;iT_C)}{B(0;T)} \quad (\text{s. } 66) $$

$$ f_t = S_t - \sum_{i=m}^{k} rF\,B(t;iT_C) - X\,B(t;T), \quad T_m = mT_C \text{ första kupongdatum efter } t \quad (\text{s. } 67) $$

`S_t` är obligationens (dirty) pris vid `t`.

### Forward på valuta, Example 13–14 (s. 68–71)

Portfolio 1 = long forward + HKD-bond face `X`; Portfolio 2 = utländsk zero-coupon bond med face 1 (kostar `S_0 B_F(0;T)` HKD):

$$ X = \frac{S_0\,B_F(0;T)}{B(0;T)}, \qquad f_t = S_t\,B_F(t;T) - X\,B(t;T) \quad (\text{s. } 69) $$

**Ex 14 (s. 70–71):** 18-mån forward på 500 EUR, `S_0 = 9` HKD/EUR, 18-mån spot HKD 1.8 %, EUR 2.1 % (annual effective). Efter 6 mån: `S_0.5 = 8.8`, HKD +0.3 % (12-mån blir 1.8 %), EUR −0.1 % (12-mån blir 2.0 %).

$$ X = \frac{500\cdot 9/(1.021)^{1.5}}{1/(1.018)^{1.5}} = 4480.18, \qquad f_{0.5} = \frac{500\cdot 8.8}{1.02} - \frac{X}{1.018} \approx -87.24 $$

Facit skriver `X = 4480.1181` och `f_0.5 ≈ −87.1764` — se avsnitt 7(e).

## 6. Forward rate agreement (FRA)

### Definition och betalningsflöde (s. 72–73)

Notional `N`, period `[T1,T2]`. Vid `T2` betalar fixed-betalaren (long, låntagaren) `N K_[T1,T2]` och får `N R_[T1,T2]`; nettoutbyte `N(R_[T1,T2] − K_[T1,T2])`. Ingen principal byts. Låntagarens nettoränta blir `N K_[T1,T2]` (s. 73).

### Fair forward rate (s. 73–75)

Portfolio 1 = long FRA + short `T1`-bond face `N` (refinansiera `N` vid `T1` till `K`); Portfolio 2 = short `T2`-bond face `N(1+K)`. Båda betalar `−N(1+K)` vid `T2`:

$$ f_0 - N B(0;T_1) = -N(1+K_{[T_1,T_2]})B(0;T_2), \quad f_0 = 0 \;\Rightarrow\; K_{[T_1,T_2]} = \frac{B(0;T_1)}{B(0;T_2)} - 1 \quad (\text{s. } 74) $$

$$ (1+R_{[0,T_1]})(1+K_{[T_1,T_2]}) = 1 + R_{[0,T_2]} \quad (\text{kedjeprodukten, s. } 75) $$

| Kvotering av forward rate | Formel (s. 75–76) |
|---|---|
| Annual effective `f_[T1,T2]` | `(1+f)^(T2−T1) = B(0;T1)/B(0;T2)` ⇒ `f = (B(0;T1)/B(0;T2))^(1/(T2−T1)) − 1 = ((1+L_[0,T2])^T2/(1+L_[0,T1])^T1)^(1/(T2−T1)) − 1` |
| Kontinuerlig | `e^(f(T2−T1)) = B(0;T1)/B(0;T2)` ⇒ `f = (L_[0,T2]·T2 − L_[0,T1]·T1)/(T2 − T1)` |

### Värde av pågående FRA (härledd ur s. 73–74, ej explicit formel i anteckningen)

Samma två portföljer vid tid `t ≤ T1`, lång position (fixed-betalare):

$$ f_t = N\,B(t;T_1) - N\,(1+K_{[T_1,T_2]})\,B(t;T_2) = N\,B(t;T_2)\,\bigl(K^{(t)}_{[T_1,T_2]} - K_{[T_1,T_2]}\bigr) $$

där `K^(t) = B(t;T1)/B(t;T2) − 1` är dagens forward rate. Kostnaden att neutralisera positionen i Ex 21 (s. 91) är exakt `−f_0.5`.

### Spot från forward, Example 15 (s. 77–78)

| (a) spot annual effective | 6 mån 1.5 %, 2 år 1.75 % | `(1.015)^0.5 (1+f_[0.5,2])^1.5 = (1.0175)^2` ⇒ `f_[0.5,2] = 0.018335` |
|---|---|---|
| (b) 6-mån forward rates annual effective | now 1.6 %, 0.5 y 1.6 %, 1 y 1.7 %, 1.5 y 1.75 % | `1+R_[0,2] = 1.016^0.5·1.016^0.5·1.017^0.5·1.0175^0.5 = 1.033526` ⇒ `L_[0,2] = 1.033526^(1/2) − 1 = 0.016625` |

Allmänt: `1 + R_[0,T2] = (1+R_[0,T1])(1+K_[T1,T2])`, kedja flera perioder efter varandra och annualisera sist.

### Innehåll efter s. 78

**Example 16 – zero-coupon-pris som produkt av forward rates (s. 79–81)**

$$ B(0;nT) = \frac{1}{1+R_{[0,T]}}\prod_{i=1}^{n-1}\frac{1}{1+K_{[iT,(i+1)T]}}, \qquad 1+K_{[iT,(i+1)T]} = \frac{1+R_{[0,(i+1)T]}}{1+R_{[0,iT]}} $$

Tolkning: `K` är "förväntat värde" av det slumpmässiga `R`; motiverar short rate model (bara `T`-års spot behövs) (s. 81).

**Example 17 – kupongobligation via forward rates (s. 82).** `F=500, c=4 %` årligen, 3 år; 1-års forward rates kontinuerliga: now 2.3 %, 1 y 2.3 %, 2 y 2.5 %:
`V_0 = 20/e^0.023 + 20/(e^0.023 e^0.023) + 520/(e^0.023 e^0.023 e^0.025) ≈ 523.0062`.

**Synthetic forward (s. 83–88).** Portfölj vars payoff = forwardens terminal-payoff. Motivering (s. 83–84): long 2-års forward, `S_0 = 50`, spot 4 % ⇒ `X = 50(1.04)^2 = 54.08`; efter 1 år `S_1 = 45`: sätt in `X/1.04 ≈ 52` och short-sell tillgången för 45 ⇒ förlusten låses till `7`.

| Underliggande | Synthetic long forward (lång position) | Sida |
|---|---|---|
| Kupongobligation (Ex 18) | köp obligationen, short `T`-bond face `X`, short `iT_C`-bonds face `rF` för `i = 1..k` | s. 85–86 |
| Valuta (Ex 19) | köp utländsk `T`-bond face 1, short inhemsk `T`-bond face `X`; kostnad `S_0 B_F(0;T) − X B(0;T)` | s. 87 |
| FRA (Ex 20) | köp `T1`-bond face `N`, återinvestera till `R_[T1,T2]`; short `T2`-bond face `N(1+K)` ⇒ payoff `N R − N K` | s. 88 |

Short-versionen fås genom att vända alla positioner (s. 86). Användning: begränsa förlust, låsa vinst, utnyttja arbitrage (s. 89).

**Example 21 – neutralisera long FRA (s. 89–91).** `N = 100000`, `[T1,T2] = [1,1.5]`; spot 6 mån 1.6 %, 1 år 1.9 %, 1.5 år 2 % (annual effective):
`(1.019)(1+f_[1,1.5])^0.5 = (1.02)^1.5` ⇒ `f_[1,1.5] = 0.022003`, `K_[1,1.5] = 1.022003^0.5 − 1`.
Efter 6 mån (spot 1.1 / 1.4 / 1.6 %): `(1.011)^0.5(1+f*)^0.5 = 1.014` ⇒ `f* = 0.017009` < `f` ⇒ låntagaren förlorar. Motportfölj = synthetic short FRA: long 1-års bond face `N(1+K)`, short 0.5-års bond face `N`.
`Cost = N(1+K)/1.014 − N/(1.011)^0.5 ≈ 243.8903` (s. 91; med oavrundat `K` fås 243.888).

**Example 22 – låsa vinst i short FRA (s. 92–93).** Flat 3 %, short 1-års FRA som startar om 2 år, `K_[2,3] = 3 %`. Efter 1 år flat 2.3 %. Bygg synthetic long FRA (köp 1-års bond face `N`, short 2-års bond face `N(1+K)`):
`Nettokassaflöde vid t=1 = N(1.03)/(1.023)^2 − N/1.023 = 0.006689 N` (låst vinst per notional).

**Example 23 – arbitrage i forward price på kupongobligation (s. 94–96).** Spot 3 / 3.1 / 3.4 %, `F=1000, c=4 %`, marknadens 1-års forward price 1000.
`S_0 = 40/1.03 + 40/1.031^2 + 1040/1.034^3 = 1017.21`, no-arbitrage `f_[0,1] = S_0(1.03) − 40 = 1007.73 ≠ 1000`.
Strategi: long forward (kostnad 0, payoff `S_1 − 1000`), köp 1-års bond face `1040` (kostnad `1040/1.03`), short-sell obligationen (`+1017.21`, payoff `−S_1 − 40`). `V_0 = −7.5 < 0`, `V_T = 0`.

**Example 24 – arbitrage i FRA (s. 97–98).** Spot 3 / 3.2 / 3.3 %, marknadens `f_[1,3] = 3.8 %`. No-arbitrage: `(1.03)(1+f)^2 = (1.033)^3` ⇒ `f ≈ 0.0345`. Strategi (`N=1`): short FRA (`K_[1,3] = 1.038^2 − 1 ≈ 0.077444`), köp 1-års bond face 1 (`1/1.03`) och återinvestera, short 3-års bond face `1+K` (`−(1+K)/1.033^3`). `V_0 = −0.0066`, `V_T = 0`.

**Example 25 – covered interest rate arbitrage (s. 99–101).** HKD 0.1 %, USD 2 %, `S_0 = 7.85`. Låna HKD, köp USD, investera, växla tillbaka: vinst 1900 om kursen står still, men förlust om USD faller (7.6 ⇒ −1348.41). Säkra med forward:
`K = S_0 B_USD(0;1)/B_HKD(0;1) = (7.85/1.02)/(1/1.001) ≈ 7.7037745` ⇒ vinst 0. Om marknadens `K > 7.7037745`: strategin ovan + short forward ger riskfri vinst. Om `K <`: låna USD, investera HKD, long forward: `78500(1.001) − 10200K > 0`.

## 7. Vanliga fel

- **(a) Annualisering:** exponenten är `1/(antal ÅR)`, inte `1/(antal månader)`. 6-mån periodränta `R` ⇒ `L = (1+R)^(1/0.5) − 1 = (1+R)^2 − 1`; 18-mån forward ⇒ `(1+f)^1.5` (s. 75, 78).
- **(b) LIBOR är nominell:** kupong = `F·L/m` (s. 53). "Spot rate" utan tillägg är i uppgifterna oftast annual effective, då är `R_[0,t] = (1+s)^t − 1` och `B(0;t) = (1+s)^(−t)`. Ex 7 (s. 42) är undantaget där LIBOR kvoteras annual effective — läs noten i uppgiften.
- **(c) Pris vid framtida tid `t`:** nuvärdet av *återstående* kassaflöden sett från `t` med den yield/termstruktur som gäller vid `t` (Ex 1b, s. 12; Ex 4b, s. 26). Inte `P_0(1+i)^t`, och kuponger som redan betalats ska bort.
- **(d) FRN vid parallellskift:** nästa kupong sätts bara om på kupongdatum; mellan datum är den låst (Ex 10, s. 59: kupongen 25 kvarstår, bara diskonteringen `B(0.5;1)` ändras). Priset är `F` bara *på* kupongdatum.
- **(e) Example 14:** facit skriver `X = 4480.1181` men rätt värde är `4480.18` (sifferförväxling), så `f_0.5 ≈ −87.24` snarare än `−87.18`. Metoden (s. 71) är korrekt.
- **(f) Kupongfraktion `f` vs forward rate `f`:** samma bokstav, olika saker (s. 15 resp. s. 75).
- **(g) Forward på kupongobligation:** dra bort *bara* kuponger i `(t,T]`, diskonterade till `t`, och dividera hela täljaren med `B(t;T)` (s. 66–67). Glöm inte att `S_t` är dirty price.
- **(h) FRA-tecken:** long = fixed-betalare, payoff `N(R − K)` vid `T2`. Stigande räntor gynnar long. I Ex 21 är låntagaren long och förlorar när räntan faller (s. 90).
- **(i) D_Mod-konvention:** `D_Mod = D_Mac/(1+i)` om `i` är annual effective, `D_Mac/(1+i/m)` om nominell (Ex 5 använder `1.0185`), `D_Mac` om kontinuerlig (s. 28–29). Blanda inte.
- **(j) Konvexitet:** exponenten är `t_k + 2` i täljaren, och faktorn är `t_k(t_k+1)`, inte `t_k^2` (s. 33). Andra ordningens term har `ε²/2`.
- **(k) Kedjeprodukten:** multiplicera `(1+R)`-faktorer för *periodräntor*, inte annualiserade räntor; annualisera först när hela `1+R_[0,T]` är känd (s. 78).
- **(l) Valutaforward:** `B_F` (utländsk) multiplicerar `S`, `B` (inhemsk) multiplicerar `X`; kurserna anges i HKD per enhet utländsk valuta (s. 69).

## 8. Hjälpfunktioner i `code/MATH_4511_functions.py`

Konvention i filen: `i` är alltid **annual effective**, tider i år, `t` = värderingstidpunkt. `Bond.price(i, t)` ger dirty price = PV av flöden med `t_k > t`.

| Formel (sida) | Anrop |
|---|---|
| Fixed bond `P_0(i)` (s. 10) | `Bond_fixed(F=100, T=6, m=4, c=0.06, i=(1+0.062/4)**4-1).price()` → 99.00427 (Ex 1a) |
| Pris vid `t` med ny yield (s. 12) | `b.price(i=(1+0.056/4)**4-1, t=2)` → 101.4246 (Ex 1b) |
| Spot-rate-prissättning (s. 25) | ingen direkt metod; summera `CF*B` manuellt eller använd `b.forward_value(...)` med `B=lambda t,s: ...` |
| `D_Mac` (s. 28) | `Bond_fixed(1500, 12, 4, 0.068, (1+0.074/4)**4-1).d_mac()` → 8.19332641 (Ex 5) |
| `D_Mod = D_Mac/(1+i)` (s. 28) | `b.d_mod()`; obs: delar med `1+i` (annual effective). För Ex 5:s nominella konvention: `b.d_mac()/(1+0.074/4)` → 8.0445031 |
| `C_Mod` (s. 33) | `Bond_fixed(1000, 10, 1, 0.05, 0.05).c_mod()` → 74.99768 (Ex 6) |
| 1:a/2:a ordn. approx (s. 36) | `b.first_order_approx(0.0525)` → 980.6957; `b.second_order_approx(0.0525)` → 980.93 (Ex 6a) |
| Generell kassaflödeslista | `Bond(F, m, coupons=[...], i)` – en kupong per period, `F` läggs på sista |
| FRN pris `V_t = (F R + F) B(t;T_k)` (s. 54) | `Bond_floating(1000, 2, [0.028]*6).price(i=(1+0.0265/2)**2-1, t=0.25)` → 1007.348 (Ex 10). `rates` = nominell årsränta per period, kupong `= F·rate/m` |
| FRN duration `T_k − t` (s. 56) | `Bond_floating(1000, 1, [0.025]*3).d_mac(t=0.5)` → 0.5 (Bond B, s. 59) |
| Bond A/B-tabellen (s. 58–59) | `Bond_fixed(1000, 3, 1, 0.025, 0.025).price(i=0.0225, t=0.5)` → 1018.442; `Bond_floating(1000, 1, [0.025]*3).price(i=0.0225, t=0.5)` → 1013.66 |
| Forward price `X = (S_t − PV kuponger)/B(t;T)` (s. 62, 66) | `forward_price(S_t, B_tT, pv_coupons=0.0)`; Ex 11: `forward_price(50, math.exp(-0.04))` → 52.04054 |
| Forward value `f_t` (s. 64, 67) | `forward_value(S_t, X, B_tT, pv_coupons=0.0)`; Ex 11: `forward_value(55, 52.04054, math.exp(-0.019))` → 3.9389 |
| Forward på kupongobligation (Ex 12, 23) | `Bond_fixed(1000, 3, 1, 0.04, 0.03).forward_price(T=1, B=lambda t,s: {1:1/1.03, 2:1/1.031**2, 3:1/1.034**3}[s])` → 1007.73; `.forward_value(T=1, X=1000, B=...)` → 7.50 (Ex 23) |
| Valutaforward (s. 69) | ingen egen funktion: `forward_price(S_0*B_F, B)` och `forward_value(S_t*B_F_t, X, B_t)` |
| `K_[i,j] = (1+R_[0,j])/(1+R_[0,i]) − 1` (s. 75) | `rate_between(i, j, rs)` där `rs[t] = R_[0,t]` är *periodräntor* (`(1+s_0(t))^t − 1`), t.ex. `rate_between(1, 1.5, {1: 0.019, 1.5: 1.02**1.5-1})` → 0.010942 (Ex 21) |
| FRN mellan datum via spot-dict (s. 54) | `frn_ongoing(i, j, F, t, rs)` = `F(1+K_[i,j])·B(t;j)`; `rs` måste innehålla `i`, `t`, `j` |
| Legacy-funktioner | `fixed_rate_bond(F, c, m, T, i)`, `d_mod(...)`, `c_mod(...)`, `second_order_approx(i_0, i_1, F, c, m, T)` – samma formler som klassmetoderna, `i` annual effective |
