"""Build Return_USstock.xlsx for MATH4515 L3 (Examples 9-11).

Daily log-returns of LUV, LLY, BRK-B, ADBE and DAL from 1 Jan 2011 to 31 Dec 2019,
computed from adjusted closing prices on Yahoo Finance. Column 1 is the date and
columns 2-6 are the stocks, so the lecture's R code `Return_USstock[c(2,3,4,5,6)]`
works unchanged.

Needs yfinance (installed in Anaconda base, not in .venv):
    ~/anaconda3/bin/python "MATH 4515/code/make_return_usstock.py"
"""
import os

import numpy as np
import pandas as pd
import yfinance as yf

TICKERS = ["LUV", "LLY", "BRK-B", "ADBE", "DAL"]
START, END = "2010-12-31", "2020-01-01"   # one day before so the first return is 3 Jan 2011
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Return_USstock.xlsx")

prices = yf.download(TICKERS, start=START, end=END, auto_adjust=True, progress=False)["Close"]
prices = prices[TICKERS]                      # keep the lecture's column order
returns = np.log(prices / prices.shift(1)).iloc[1:]
returns = returns.loc["2011-01-01":"2019-12-31"]

out = returns.reset_index().rename(columns={"index": "Date"})
out["Date"] = out["Date"].dt.date
out.to_excel(OUT, index=False)

print(f"wrote {os.path.relpath(OUT)}: {len(out)} rows, {out['Date'].iloc[0]} to {out['Date'].iloc[-1]}")
print("missing values per column:\n", out.isna().sum().to_string())
print("\nMLE of mu (column means):\n", returns.mean().to_string())
print("\nMLE of Sigma (divide by n):\n", returns.cov(ddof=0).to_string())
