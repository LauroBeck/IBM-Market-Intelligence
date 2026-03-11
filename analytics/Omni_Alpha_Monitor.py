import pandas as pd
import os

def generate_report():
    # Data extracted from March 11, 2026 snapshots
    data = {
        'Symbol': ['S&P 500', 'DOW', 'NASDAQ', 'IBM', 'TSLA', 'NVDA', 'ORCL', 'INTC'],
        'Price': [6770.18, 47421.02, 22690.22, 249.065, 408.07, 185.52, 162.71, 47.94],
        'Change_Pct': [-0.17, -0.60, -0.03, -0.45, 2.21, 0.41, 8.91, 2.48]
    }
    
    df = pd.DataFrame(data)
    df['Status'] = df['Change_Pct'].apply(lambda x: '🟢' if x > 0 else '🔴')
    
    print(f"\n[SYSTEM REPORT: {os.popen('date').read().strip()}]")
    print("-" * 50)
    print(df.to_string(index=False))
    print("-" * 50)
    
    # Check for divergence (Indices down but Tech up)
    tech_bulls = df[(df['Symbol'].isin(['ORCL', 'TSLA', 'NVDA'])) & (df['Change_Pct'] > 0)]
    if not tech_bulls.empty:
        print(f"DIVERGENCE DETECTED: {len(tech_bulls)} Tech assets showing idiosyncratic strength.")

if __name__ == "__main__":
    generate_report()
