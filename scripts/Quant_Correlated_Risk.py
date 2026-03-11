import pandas as pd
import numpy as np

def calculate_risk_exposure():
    # Data derived from latest Bloomberg Terminal snapshots
    # USD-INR: 92.0412 | IBM: $249.06 | TSLA: Momentum Alert
    
    data = {
        'USD_INR': [91.5, 91.8, 92.0, 92.04],
        'IBM': [251.2, 250.5, 249.8, 249.06],
        'TSLA': [235.1, 238.4, 241.0, 246.3]
    }
    df = pd.DataFrame(data)
    returns = df.pct_change().dropna()
    
    # Calculate Correlation Matrix
    corr_matrix = returns.corr()
    
    print("--- ⚖️ Quant Correlated Risk Report ---")
    print(f"IBM vs USD-INR Correlation: {corr_matrix.loc['IBM', 'USD_INR']:.4f}")
    print(f"TSLA vs USD-INR Correlation: {corr_matrix.loc['TSLA', 'USD_INR']:.4f}")
    
    if corr_matrix.loc['IBM', 'USD_INR'] < -0.7:
        print("⚠️ RISK ALERT: Strong Inverse Correlation. USD strength is suppressing IBM.")
    else:
        print("✅ STABILITY: Correlation within normal sovereign bounds.")
    print("---------------------------------------")

if __name__ == "__main__":
    calculate_risk_exposure()
