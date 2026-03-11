import yfinance as yf
import pandas as pd
import numpy as np
from rich.console import Console
from rich.table import Table
from datetime import datetime
import time

console = Console()

# ---------------------------------------
# MARKET TICKERS
# ---------------------------------------

TICKERS = {

    # TECH / AI
    "IBM": "IBM",
    "ORACLE": "ORCL",
    "MICROSOFT": "MSFT",
    "NVIDIA": "NVDA",

    # ENERGY MAJORS
    "CHEVRON": "CVX",
    "EXXON": "XOM",
    "BP": "BP",
    "SHELL": "SHEL",
    "CONOCOPHILLIPS": "COP",
    "ARAMCO": "2222.SR",

    # MACRO
    "NASDAQ": "^IXIC",
    "OIL": "CL=F",
    "GOLD": "GC=F"
}

# ---------------------------------------
# MARKET DATA ENGINE
# ---------------------------------------

def get_market_data():

    market = {}

    for name, ticker in TICKERS.items():

        try:

            t = yf.Ticker(ticker)
            hist = t.history(period="2d")

            price = float(hist["Close"].iloc[-1])
            prev = float(hist["Close"].iloc[-2])

            change = ((price - prev) / prev) * 100

            # Fix abnormal gold values
            if name == "GOLD" and price > 3000:
                price = price / 2

            market[name] = {
                "price": price,
                "change": change
            }

        except:
            market[name] = {
                "price": 0,
                "change": 0
            }

    return market


# ---------------------------------------
# PROJECTION ENGINE
# ---------------------------------------

def compute_projections(data):

    oil_factor = data["OIL"]["price"] / 100
    nasdaq_factor = data["NASDAQ"]["price"] / 20000
    gold_factor = data["GOLD"]["price"] / 2200

    projections = {}

    # TECH

    projections["IBM"] = data["IBM"]["price"] * (1 + nasdaq_factor*0.08 + gold_factor*0.02)

    projections["ORACLE"] = data["ORACLE"]["price"] * (1 + nasdaq_factor*0.12 - oil_factor*0.03)

    projections["MICROSOFT"] = data["MICROSOFT"]["price"] * (1 + nasdaq_factor*0.10)

    projections["NVIDIA"] = data["NVIDIA"]["price"] * (1 + nasdaq_factor*0.15)

    # ENERGY

    projections["CHEVRON"] = data["CHEVRON"]["price"] * (1 + oil_factor*0.12)

    projections["EXXON"] = data["EXXON"]["price"] * (1 + oil_factor*0.12)

    projections["BP"] = data["BP"]["price"] * (1 + oil_factor*0.10)

    projections["SHELL"] = data["SHELL"]["price"] * (1 + oil_factor*0.11)

    projections["CONOCOPHILLIPS"] = data["CONOCOPHILLIPS"]["price"] * (1 + oil_factor*0.13)

    projections["ARAMCO"] = data["ARAMCO"]["price"] * (1 + oil_factor*0.09)

    return projections


# ---------------------------------------
# MACRO RISK ENGINE
# ---------------------------------------

def compute_risk(data):

    oil = data["OIL"]["price"]
    gold = data["GOLD"]["price"]
    nasdaq_change = data["NASDAQ"]["change"]

    if oil > 95:
        return "ENERGY SHOCK"

    if gold > 2300:
        return "SAFE HAVEN FLOW"

    if nasdaq_change < -2:
        return "TECH SELL-OFF"

    return "NORMAL MARKET"


# ---------------------------------------
# DASHBOARD
# ---------------------------------------

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

    assets = [

        "IBM","ORACLE","MICROSOFT","NVIDIA",

        "CHEVRON","EXXON","BP","SHELL",
        "CONOCOPHILLIPS","ARAMCO"
    ]

    for asset in assets:

        table.add_row(
            asset,
            f"${data[asset]['price']:.2f}",
            f"{data[asset]['change']:.2f} %",
            f"${projections[asset]:.2f}"
        )

    # MACRO

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


# ---------------------------------------
# REAL-TIME LOOP
# ---------------------------------------

if __name__ == "__main__":

    while True:

        try:

            display_terminal()

            time.sleep(30)

        except KeyboardInterrupt:

            print("\nTerminal stopped.")

            break
