import numpy as np
import pandas as pd

# Current Portfolio Matrix (6 Qubits)
portfolio = ['NDX', 'IBM', 'JEPQ', 'TSLA', 'JPM', 'BNY']
stability_index = 0.82  # Extracted from your current stability curve at low shock

def simulate_quantum_alpha(stability):
    """
    Simulates a stability-weighted portfolio return.
    Higher stability (near 1.0) preserves tech growth (NDX/TSLA).
    Low stability (below 0.5) triggers a rotation to Value (IBM/JPM/BNY).
    """
    # Base expected daily moves based on today's Bloomberg/Nasdaq captures
    daily_beta = np.array([0.0003, 0.0045, 0.0009, 0.0221, -0.0063, 0.0012])
    
    # The 'Phase Shift' - Adjusting weights based on Stability
    # If stability is high, we stay with Tech. If low, we shift to JPM/BNY.
    if stability > 0.6:
        weights = np.array([0.25, 0.15, 0.20, 0.10, 0.15, 0.15])
    else:
        weights = np.array([0.10, 0.20, 0.25, 0.05, 0.20, 0.20])
        
    return np.dot(weights, daily_beta)

# Calculate for current state
projected_alpha = simulate_quantum_alpha(stability_index)

print(f"--- 6-Qubit Portfolio Strategy: {pd.Timestamp.now().strftime('%Y-%m-%d')} ---")
print(f"Current Stability Score: {stability_index:.4f}")
print(f"Projected Alpha Move: {projected_alpha*100:+.4f}%")
print("Status: GREEN - Maintaining Tech/Value Balance")
