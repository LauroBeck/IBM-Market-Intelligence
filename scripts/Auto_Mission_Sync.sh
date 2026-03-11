#!/bin/bash
# Mission Automation & Git Sync for IBM-Market-Intelligence

LOG_FILE="MISSION_LOG.md"
REPO_URL="https://github.com/LauroBeck/IBM-Market-Intelligence.git"

while true; do
    # 1. Update the Mission Log
    echo "---" >> $LOG_FILE
    echo "## 🕒 IBM MARKET INTEL SYNC: $(date '+%Y-%m-%d %H:%M:%S')" >> $LOG_FILE
    echo '```text' >> $LOG_FILE
    python3 scripts/Mission_Control_Center.py >> $LOG_FILE
    echo '```' >> $LOG_FILE
    
    # 2. Git Operations targeting IBM-Market-Intelligence
    git add .
    git commit -m "System Update: Intraday IBM/Market Intelligence Snapshot [$(date '+%Y-%m-%d %H:%M')]"
    
    # Push specifically to the main branch
    git push origin main
    
    echo "Sync to IBM-Market-Intelligence successful. Resting..."
    sleep 3600
done
