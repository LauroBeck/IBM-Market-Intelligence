import pandas as pd
import numpy as np
from datetime import datetime

# ----------------------------
# Market Input Data
# (example values from Bloomberg screen)
# ----------------------------

market_data = {

    "nasdaq_futures": 24976.75,
    "sp500_futures": 6790.00,
    "oil_wti": 85.75,
    "gold": 2200,
    "dollar_index": 1200.45,

    "ibm_price": 196.50,
    "oracle_price": 162.36
}

# ----------------------------
# Factor Engine
# ----------------------------

def compute_macro_factors(data):

    oil_factor = data["oil_wti"] / 100
    ai_factor = data["nasdaq_futures"] / 25000
    gold_factor = data["gold"] / 2200

    return oil_factor, ai_factor, gold_factor


# ----------------------------
# Projection Model
# ----------------------------

def project_stocks(data):

    oil_factor, ai_factor, gold_factor = compute_macro_factors(data)

    # Oracle = stronger AI beta
    oracle_projection = data["oracle_price"] * (
        1 + (ai_factor * 0.12) - (oil_factor * 0.03)
    )

    # IBM = enterprise + hybrid cloud stability
    ibm_projection = data["ibm_price"] * (
        1 + (ai_factor * 0.08) - (oil_factor * 0.02) + (gold_factor * 0.01)
    )

    return oracle_projection, ibm_projection


# ----------------------------
# Risk Model
# ----------------------------

def classify_risk(data):

    if data["oil_wti"] > 95:
        return "GEOPOLITICAL SHOCK"

    if data["gold"] > 2300:
        return "SAFE HAVEN FLOW"

    return "NORMAL"


# ----------------------------
# Run Engine
# ----------------------------

oracle_target, ibm_target = project_stocks(market_data)
risk_state = classify_risk(market_data)

print("\nGLOBAL AI CLOUD PROJECTION ENGINE\n")

print("Date:", datetime.now())
print("Risk Level:", risk_state)

print("\nStock Projections\n")

print(f"Oracle Target: ${oracle_target:.2f}")
print(f"IBM Target:    ${ibm_target:.2f}")
