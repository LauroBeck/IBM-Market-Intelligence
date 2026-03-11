import numpy as np
import pandas as pd

class CentralBankRiskEngine:

    def __init__(self, bond_issuance, fx_rate, gdp_growth):
        self.bond_issuance = bond_issuance
        self.fx_rate = fx_rate
        self.gdp_growth = gdp_growth

    def debt_to_gdp(self):
        return self.bond_issuance / (1 + self.gdp_growth)

    def fx_shock(self, shock_percent):
        return self.fx_rate * (1 + shock_percent)

    def stress_scenario(self, rate_shock, fx_shock_percent):
        stressed_debt = self.debt_to_gdp() * (1 + rate_shock)
        stressed_fx = self.fx_shock(fx_shock_percent)

        return {
            "Stressed Debt Level": stressed_debt,
            "Stressed FX Rate": stressed_fx
        }


# Example based on Bloomberg image context
engine = CentralBankRiskEngine(
    bond_issuance=4.4e12,   # 4.4 trillion yuan
    fx_rate=6.88,          # USD/CNY from image
    gdp_growth=0.05        # 5% GDP target
)

scenario = engine.stress_scenario(
    rate_shock=0.02,       # +2% interest shock
    fx_shock_percent=-0.03 # 3% currency strengthening
)

print("Central Bank Stress Scenario:")
print(scenario)
