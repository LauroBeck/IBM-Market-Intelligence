import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

def create_scorecard():
    # March 11, 2026 Snapshot Data
    data = {
        'Asset': ['S&P 500', 'NASDAQ', 'IBM', 'TSLA', 'ORCL'],
        'Performance': [-0.17, -0.03, -0.45, 2.21, 8.91]
    }
    df = pd.DataFrame(data)
    
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['#ff4b4b' if x < 0 else '#00ff7f' for x in df['Performance']]
    bars = ax.barh(df['Asset'], df['Performance'], color=colors, alpha=0.8)
    
    ax.set_title(f'Institutional Alpha Scorecard | {datetime.now().strftime("%Y-%m-%d")}', fontsize=16, pad=20)
    ax.set_xlabel('Percentage Change (%)', fontsize=12)
    ax.axvline(0, color='white', linewidth=1, alpha=0.5)
    
    # Add labels
    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2, f' {width}%', 
                va='center', fontsize=10, color='white', fontweight='bold')

    plt.tight_layout()
    plt.savefig('reports/exports/alpha_scorecard_v1.png')
    print("Dashboard exported: reports/exports/alpha_scorecard_v1.png")

if __name__ == "__main__":
    create_scorecard()
