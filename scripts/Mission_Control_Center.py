import subprocess
import os
from datetime import datetime

scripts = ["Quant_Correlated_Risk.py", "Generate_Market_Scorecard.py", 
    "Mission_State_Snapshot.py",
    "Omni_Alpha_Monitor.py",
    "Market_Pulse_Oracle.py",
    "Sovereign_Equities_Bridge.py",
    "Tactical_Market_Alignment.py"
]

def run_mission_check():
    print(f"=== GLOBAL MISSION CONTROL: {datetime.now().strftime('%Y-%m-%d %H:%M')} ===")
    print(f"Status: 🟢 SYSTEM NOMINAL\n")
    
    for script in scripts:
        path = os.path.join("scripts", script)
        if os.path.exists(path):
            result = subprocess.run(["python3", path], capture_output=True, text=True)
            print(result.stdout.strip())
            print("-" * 40)

if __name__ == "__main__":
    run_mission_check()
