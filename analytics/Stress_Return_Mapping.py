import numpy as np
import pandas as pd
import plotly.graph_objects as go

# 1. Setup
vix_shocks = np.linspace(0, 0.5, 30)
k = 12.5
daily_beta = np.array([0.0003, 0.0045, 0.0009, 0.0221, -0.0063, 0.0012]) # NDX, IBM, JEPQ, TSLA, JPM, BNY

results = []

for shock in vix_shocks:
    stability = np.exp(-k * (shock**2))
    
    # Weight logic: Dynamic rotation based on stability score
    if stability > 0.6:
        # Tech/Growth Heavy
        weights = np.array([0.25, 0.15, 0.20, 0.10, 0.15, 0.15])
    else:
        # Value/Defensive Rotation (IBM/JPM/BNY)
        weights = np.array([0.10, 0.25, 0.25, 0.05, 0.20, 0.15])
        
    projected_return = np.dot(weights, daily_beta) * 100
    results.append({'Shock': shock, 'Stability': stability, 'Return': projected_return})

df = pd.DataFrame(results)

# 2. Visualize Mapping
fig = go.Figure()

# Portfolio Return Trace
fig.add_trace(go.Scatter(x=df['Shock'], y=df['Return'], name='Exp. Return (%)',
                         line=dict(color='#00ff88', width=4)))

# Stability Trace (Secondary Axis)
fig.add_trace(go.Scatter(x=df['Shock'], y=df['Stability'], name='Stability Score',
                         line=dict(color='rgba(255,255,255,0.3)', dash='dot'), yaxis='y2'))

fig.update_layout(
    title="<b>Portfolio Alpha vs. VIX Shock Intensity</b>",
    template='plotly_dark',
    paper_bgcolor='#050505', plot_bgcolor='#050505',
    yaxis=dict(title="Projected Alpha (%)", gridcolor='#222'),
    yaxis2=dict(title="Stability", overlaying='y', side='right', range=[0, 1]),
    xaxis=dict(title="VIX Shock Intensity", gridcolor='#222')
)

fig.write_image("alpha_stability_mapping.png", scale=2)
print("Mapping complete. Strategic visual saved: alpha_stability_mapping.png")
