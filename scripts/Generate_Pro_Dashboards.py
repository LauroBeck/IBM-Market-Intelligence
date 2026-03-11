import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_pro_visuals():
    # Setup styling for the "Pro" look
    plt.style.use('dark_background')
    
    # Simulate YTD Time Series Data
    dates = pd.date_range(start="2026-01-01", end=datetime.now(), freq='D')
    n = len(dates)
    
    # Simulated Evolution Data
    ibm = 280 + np.cumsum(np.random.randn(n) * 2)
    sp500 = 6800 + np.cumsum(np.random.randn(n) * 15)
    nasdaq = 23000 + np.cumsum(np.random.randn(n) * 50)
    vix = 15 + np.cumsum(np.random.randn(n) * 0.8)

    # 1. Generate the main Dashboard Preview (Multi-Index)
    fig, axs = plt.subplots(4, 1, figsize=(12, 16), sharex=True)
    fig.suptitle('IBM vs Bloomberg Scorecard | 2026', fontsize=18, color='#00d4ff')

    # Plotting each index with specific "Pro" colors
    axs[0].plot(dates, ibm, color='#5c7cff', label='IBM Evolution')
    axs[1].plot(dates, sp500, color='#ff4b4b', label='S&P 500')
    axs[2].plot(dates, nasdaq, color='#00ff7f', label='Nasdaq Composite')
    axs[3].plot(dates, vix, color='#ffa500', label='VIX Index')

    for ax in axs:
        ax.grid(True, alpha=0.1)
        ax.legend(loc='upper right', fontsize=10)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('reports/exports/multi_index_dashboard.png')
    
    # 2. Generate the specific Sovereign Stress Projection
    # (Matches the green "Hedge Trigger" curve from your screenshot)
    plt.figure(figsize=(10, 6))
    x = np.linspace(0, 0.5, 100)
    y = np.exp(-10 * (x**2)) # Decay curve for stability
    plt.plot(x, y, color='#00ff7f', linewidth=3, marker='o', markevery=10)
    plt.fill_between(x, y, color='#00ff7f', alpha=0.1)
    plt.annotate('INFLECTION: HEDGE TRIGGER', xy=(0.22, 0.6), xytext=(0.15, 0.65),
                 arrowprops=dict(arrowstyle='->', color='orange'), color='orange')
    plt.title('Sovereign Stress Simulation | Green Target: IBM, JPM, NDX')
    plt.xlabel('VIX Shock Intensity')
    plt.ylabel('Stability Score (Z-Expectation)')
    plt.savefig('reports/exports/sovereign_stress_projection_v2.png')

    print("Pro Dashboards generated in reports/exports/")

if __name__ == "__main__":
    generate_pro_visuals()
