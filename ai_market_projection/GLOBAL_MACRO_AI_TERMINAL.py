import yfinance as yf
import pandas as pd
import numpy as np
from rich.console import Console
from rich.table import Table
from datetime import datetime
import time

console = Console()

# ---------------------------------
# Market Tickers
# ---------------------------------

TICKERS = {
    "IBM": "IBM",
    "ORACLE": "ORCL",
    "MICROSOFT": "MSFT",
    "NVIDIA": "NVDA",
    "NASDAQ": "^IXIC",
    "OIL": "CL=F",
    "GOLD": "GC=F"
}

# ---------------------------------
# Market Data Loader
# ---------------------------------

def get_market_data():

    market = {}

    for name, ticker in TICKERS.items():

        t = yf.Ticker(ticker)
        hist = t.history(period="2d")

        price = hist["Close"].iloc[-1]
        prev = hist["Close"].iloc[-2]

        change = ((price - prev) / prev) * 100

        market[name] = {
            "price": price,
            "change": change
        }

    return market

# ---------------------------------
# Projection Model
# ---------------------------------

def compute_projections(data):

    oil_factor = data["OIL"]["price"] / 100
    nasdaq_factor = data["NASDAQ"]["price"] / 20000
    gold_factor = data["GOLD"]["price"] / 2200

    projections = {}

    projections["ORACLE"] = data["ORACLE"]["price"] * (1 + nasdaq_factor*0.12 - oil_factor*0.03)
    projections["IBM"] = data["IBM"]["price"] * (1 + nasdaq_factor*0.08 + gold_factor*0.02)
    projections["MICROSOFT"] = data["MICROSOFT"]["price"] * (1 + nasdaq_factor*0.10)
    projections["NVIDIA"] = data["NVIDIA"]["price"] * (1 + nasdaq_factor*0.15)

    return projections

# ---------------------------------
# Risk Indicator
# ---------------------------------

def compute_risk(data):

    oil = data["OIL"]["price"]
    gold = data["GOLD"]["price"]

    if oil > 95:
        return "GEOPOLITICAL SHOCK"

    if gold > 2300:
        return "SAFE HAVEN FLOW"

    return "NORMAL MARKET"

# ---------------------------------
# Terminal Display
# ---------------------------------

def display_terminal():

    console.clear()

    data = get_market_data()
    projections = compute_projections(data)
    risk = compute_risk(data)

    table = Table(title="GLOBAL MACRO AI TERMINAL")

    table.add_column("Asset")
    table.add_column("Price")
    table.add_column("Change %")
    table.add_column("Projection")

    for asset in ["IBM","ORACLE","MICROSOFT","NVIDIA"]:

        table.add_row(
            asset,
            f"${data[asset]['price']:.2f}",
            f"{data[asset]['change']:.2f} %",
            f"${projections[asset]:.2f}"
        )

    table.add_row(
        "NASDAQ",
        f"{data['NASDAQ']['price']:.0f}",
        f"{data['NASDAQ']['change']:.2f} %",
        "-"
    )

    table.add_row(
        "OIL",
        f"${data['OIL']['price']:.2f}",
        f"{data['OIL']['change']:.2f} %",
        "-"
    )

    table.add_row(
        "GOLD",
        f"${data['GOLD']['price']:.2f}",
        f"{data['GOLD']['change']:.2f} %",
        "-"
    )

    console.print(table)

    console.print("\nMarket Risk Level:", risk)
    console.print("Last Update:", datetime.now())

# ---------------------------------
# Real-time loop
# ---------------------------------

if __name__ == "__main__":

    while True:

        try:
            display_terminal()
            time.sleep(30)

        except KeyboardInterrupt:
            print("\nTerminal stopped.")
            break
