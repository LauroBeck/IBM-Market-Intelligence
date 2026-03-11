import pandas as pd
# Focus: Multi-asset edge detection
data = {'Asset': ['SPX', 'NDX', 'IBM', 'TSLA'], 'Alpha_Score': [0.12, 0.45, -0.10, 0.88]}
df = pd.DataFrame(data)
print("--- Omni Alpha Monitor: Intraday Edge ---")
print(df.sort_values(by='Alpha_Score', ascending=False))
