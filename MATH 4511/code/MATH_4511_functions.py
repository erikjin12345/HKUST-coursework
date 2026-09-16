import math
import matplotlib.pyplot as plt
import numpy as np


class Bond:
    """Generell kupongobligation med en lista av kuponger, en per period.

    F        : nominellt belopp
    m        : antal kupongperioder per år
    coupons  : lista med kupongbelopp, en per period (längd = T*m)
    i        : årlig effektiv ränta som används om inget annat anges
    """

    def __init__(self, F, m, coupons, i):
        self.F = F
        self.m = m
        self.coupons = list(coupons)
        self.n = len(self.coupons)          # antal perioder
        self.T = self.n / m                 # löptid i år
        self.i = i

    def cash_flows(self):
        """Lista med (tid i år, kassaflöde). Nominellt belopp läggs på sista kupongen."""
        cf = [(k / self.m, self.coupons[k - 1]) for k in range(1, self.n + 1)]
        t_last, c_last = cf[-1]
        cf[-1] = (t_last, c_last + self.F)
        return cf

    def _rate(self, i):
        return self.i if i is None else i

    def price(self, i=None, t=0):
        """Pris (dirty) vid tid t år, dvs nuvärdet av alla kassaflöden efter t."""
        i = self._rate(i)
        return sum(CF / (1 + i) ** (tk - t) for tk, CF in self.cash_flows() if tk > t)

    def d_mac(self, i=None, t=0):
        """Macaulay-duration i år, sett från tid t."""
        i = self._rate(i)
        P = self.price(i, t)
        return sum((tk - t) * CF / (1 + i) ** (tk - t)
                   for tk, CF in self.cash_flows() if tk > t) / P

    def d_mod(self, i=None, t=0):
        """Modifierad duration, D_mac / (1 + i)."""
        i = self._rate(i)
        return self.d_mac(i, t) / (1 + i)

    def c_mod(self, i=None, t=0):
        """Konvexitet, sett från tid t."""
        i = self._rate(i)
        P = self.price(i, t)
        num = sum((tk - t) * (tk - t + 1) * CF / (1 + i) ** (tk - t)
                  for tk, CF in self.cash_flows() if tk > t)
        return num / ((1 + i) ** 2 * P)

    def first_order_approx(self, i_1, i_0=None, t=0):
        i_0 = self._rate(i_0)
        eps = i_1 - i_0
        return self.price(i_0, t) * (1 - eps * self.d_mod(i_0, t))

    def second_order_approx(self, i_1, i_0=None, t=0):
        i_0 = self._rate(i_0)
        eps = i_1 - i_0
        return self.price(i_0, t) * (1 - eps * self.d_mod(i_0, t)
                                     + eps ** 2 / 2 * self.c_mod(i_0, t))


    # ---- Forwardkontrakt på obligationen (Example 12, s. 65-67) ----

    def _df(self, t, s, i=None, B=None):
        """Diskonteringsfaktor B(t; s). Om B ges är det en funktion B(t, s) (termstruktur),
        annars används flat årlig effektiv ränta i."""
        if B is not None:
            return B(t, s)
        i = self._rate(i)
        return (1 + i) ** -(s - t)

    def _pv_cash_flows(self, t, i=None, B=None, upto=None):
        """Nuvärde vid tid t av kassaflödena efter t (och senast vid upto, om det anges)."""
        return sum(CF * self._df(t, tk, i, B)
                   for tk, CF in self.cash_flows()
                   if tk > t and (upto is None or tk <= upto))

    def forward_price(self, T, i=None, t=0, B=None):
        """Leveranspris X vid tid t för ett forwardkontrakt på obligationen med leverans vid T.

            X = ( S_t - sum_{t < T_i <= T} CF_i * B(t; T_i) ) / B(t; T)

        Kupongerna som betalas under (t, T] tillfaller säljaren och dras därför bort.
        S_t är obligationens (dirty) pris vid t. Kräver t < T < löptiden."""
        if not t < T < self.T:
            raise ValueError("kräver t < T < obligationens löptid")
        S_t = self._pv_cash_flows(t, i, B)
        pv_coupons = self._pv_cash_flows(t, i, B, upto=T)
        return forward_price(S_t, self._df(t, T, i, B), pv_coupons)

    def forward_value(self, T, X, i=None, t=0, B=None):
        """Värde f_t (lång position) av ett pågående forwardkontrakt med leveranspris X.

            f_t = S_t - sum_{t < T_i <= T} CF_i * B(t; T_i) - X * B(t; T)

        Vid t = 0 med X = forward_price(T) blir värdet 0 (no arbitrage)."""
        if not t < T < self.T:
            raise ValueError("kräver t < T < obligationens löptid")
        S_t = self._pv_cash_flows(t, i, B)
        pv_coupons = self._pv_cash_flows(t, i, B, upto=T)
        return forward_value(S_t, X, self._df(t, T, i, B), pv_coupons)


class Bond_fixed(Bond):
    """Obligation med fast kupongränta c (årlig, betalas m gånger per år)."""

    def __init__(self, F, T, m, c, i):
        self.c = c
        Bond.__init__(self, F, m, [F * c / m] * (T * m), i)


class Bond_floating(Bond):
    """Obligation med flytande kupong. rates = en ränta per period (lista eller dict),
    kvoterad som årlig nominell ränta. Kupong per period = F * rate / m.

    Bara nästa kupong är känd (den låstes vid förra omsättningen). Vid nästa
    kupongdatum sätts räntan om och obligationen är då värd par. Sett från tid t
    finns därför bara ett relevant kassaflöde: F + nästa kupong."""

    def __init__(self, F, m, rates, i=None):
        rates = list(rates.values()) if isinstance(rates, dict) else list(rates)
        self.rates = rates
        if i is None:
            i = rates[0]
        Bond.__init__(self, F, m, [F * r / m for r in rates], i)

    def _next_cash_flow(self, t):
        """(tid, F + nästa kupong) för första kupongdatum efter t."""
        for k in range(1, self.n + 1):
            tk = k / self.m
            if tk > t:
                return tk, self.F + self.coupons[k - 1]
        raise ValueError("t ligger efter sista kupongdatumet")

    def price(self, i=None, t=0):
        i = self._rate(i)
        tk, CF = self._next_cash_flow(t)
        return CF / (1 + i) ** (tk - t)

    def d_mac(self, i=None, t=0):
        tk, _ = self._next_cash_flow(t)
        return tk - t

    def c_mod(self, i=None, t=0):
        i = self._rate(i)
        tk, _ = self._next_cash_flow(t)
        tau = tk - t
        return tau * (tau + 1) / (1 + i) ** 2


def fixed_rate_bond(F, c, m, T, i):
    coupons = F*c/m
    cash_flows = sum(
        coupons/(1+i)**(k/m) for k in range(1, T*m+1)
    ) + F/(1+i)**(T)
    return cash_flows

def d_mod(F, c, m, T, i):
    coupons = F*c/m
    P0 = fixed_rate_bond(F, c, m, T, i)
    d_mod = 1/(1+i) * (sum(k/m * coupons/(1+i)**(k/m) for k in range(1, T*m+1)) + T*F/(1+i)**T)/(P0)
    return d_mod

def c_mod(F, c, m, T, i):
    coupons = F*c/m
    P0 = fixed_rate_bond(F, c, m, T, i)
    c_mod = (sum(k/m*(k/m+1)* coupons/(1+i)**(k/m) for k in range(1, T*m+1)) + (T*(T+1)*F/(1+i)**T))/((1+i)**2 * P0)
    return c_mod

def second_order_approx(i_0, i_1, F, c, m, T):
    coupons = F*c/m
    P0 = fixed_rate_bond(F, c, m, T, i_0)
    eps = i_1 - i_0
    P1 = P0 * (1 -eps * d_mod(F, c, m, T, i_0) + eps**2/2 * c_mod(F, c, m, T, i_0))
    return P1

def rate_between(i, j, rs):
    #rs is a dictionary of rates for different maturities
    R_ij = (1+rs[j])/(1+rs[i]) - 1
    return R_ij

def frn_ongoing(i, j, F, t, rs):
    R_ij = rate_between(i, j, rs)
    B_tj = 1/(1+rate_between(t, j, rs))
    V = F*(1+R_ij)*B_tj
    return V


# ---- Forwardkontrakt, generella formler (s. 61-67) ----

def forward_price(S_t, B_tT, pv_coupons=0.0):
    """Leveranspris (forwardpris) X vid tid t för leverans vid T:

        X = (S_t - pv_coupons) / B(t; T)

    S_t         : tillgångens pris vid t
    B_tT        : diskonteringsfaktor B(t; T)
    pv_coupons  : nuvärde vid t av utbetalningar (kuponger) under (t, T] som säljaren
                  behåller. 0 för en tillgång utan utdelning (Example 11)."""
    return (S_t - pv_coupons) / B_tT


def forward_value(S_t, X, B_tT, pv_coupons=0.0):
    """Värde f_t av ett pågående forwardkontrakt (lång position) med leveranspris X:

        f_t = S_t - pv_coupons - X * B(t; T)"""
    return S_t - pv_coupons - X * B_tT
