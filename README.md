# IBM & Bloomberg Market Intelligence Dashboard
`pro version` `v1.0.0-pro` `html 99.7%`

A professional-grade financial visualization suite.

## 📊 Dashboard Preview
![Dashboard Preview](https://raw.githubusercontent.com/LauroBeck/IBM-Market-Intelligence/main/reports/exports/sovereign_stress_projection_v2.png)

### 🚀 Pro Features
* **IBM Evolution**: Tracking IBM's recovery from its 22-week low with Bollinger Bands.
* **Global Indices**: Real-time tracking of S&P 500, Nasdaq, Dow Jones, and VIX.
* **YTD Scorecard**: Automated performance labels calculated for the 2026 trading year.
* **Multi-Format Export**: Generates high-res static PNGs and interactive HTML reports.

---

## 🏛 Institutional Series (Automated Alpha Architecture)
> **Note**: These components run autonomously via the `Mission_Control_Center.py` to provide intraday desk-analyst signals.

<details>
<summary><b>Click to expand Institutional Logic & Scripts</b></summary>

### 🛠 Operational Series
* **Omni_Alpha_Monitor.py**: Multi-asset edge detection (Current Focus: TSLA/NDX).
* **Market_Pulse_Oracle.py**: Specific idiosyncratic breakout tracking (e.g., ORCL +8.91%).
* **Sovereign_Equities_Bridge.py**: FX/Equity correlation mapping (USD-INR vs Tech).
* **Tactical_Market_Alignment.py**: Defensive rotation trigger logic based on VIX thresholds.

### 🤖 Automation Workflow
The system performs an **Automated Sync** every hour, appending real-time terminal data to the `MISSION_LOG.md` and syncing directly with this repository.
</details>

---
*Last Mission Sync: $(date '+%Y-%m-%d %H:%M') | Architecture: 6-Qubit Quantum Alpha*
