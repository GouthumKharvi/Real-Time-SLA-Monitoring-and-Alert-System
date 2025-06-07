
import schedule
import time
from sla_monitor import run_sla_check

def job():
    print("Running SLA check...")
    run_sla_check()

# Run every 10 seconds (change to .hourly or .daily as needed)
schedule.every(10).seconds.do(job)

print("Starting SLA monitoring... Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
