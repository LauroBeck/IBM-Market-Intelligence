import yfinance as yf
import pandas as pd
import numpy as np
from rich.console import Console
from rich.table import Table

console = Console()

# -----------------------------
# Download Market Data
# -----------------------------

tickers = {
    "IBM": "IBM",
    "ORACLE": "ORCL",
    "NASDAQ": "^IXIC",
    "OIL": "CL=F",
    "GOLD": "GC=F"
}

data = {}

for name, ticker in tickers.items():
    t = yf.Ticker(ticker)
    hist = t.history(period="2d")
    data[name] = hist["Close"].iloc[-1]

# -----------------------------
# Factor Model
# -----------------------------

oil_factor = data["OIL"] / 100
nasdaq_factor = data["NASDAQ"] / 20000
gold_factor = data["GOLD"] / 2200

# -----------------------------
# Projection Engine
# -----------------------------

oracle_projection = data["ORACLE"] * (1 + nasdaq_factor * 0.12 - oil_factor * 0.03)

ibm_projection = data["IBM"] * (1 + nasdaq_factor * 0.08 + gold_factor * 0.02)

# -----------------------------
# Display Terminal
# -----------------------------

table = Table(title="AI CLOUD PROJECTION TERMINAL")

table.add_column("Asset")
table.add_column("Current Price")
table.add_column("Projected Price")

table.add_row(
    "Oracle",
    f"${data['ORACLE']:.2f}",
    f"${oracle_projection:.2f}"
)

table.add_row(
    "IBM",
    f"${data['IBM']:.2f}",
    f"${ibm_projection:.2f}"
)

console.print(table)

print("\nMacro Factors")
print("Oil Factor:", round(oil_factor, 3))
print("Nasdaq Factor:", round(nasdaq_factor, 3))
print("Gold Factor:", round(gold_factor, 3))
