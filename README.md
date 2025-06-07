
# SLA Monitoring System

A Python-based SLA Monitoring system that checks service metrics, detects SLA violations, sends email alerts, logs violations, and displays a real-time dashboard with Streamlit.

---

## 📌 Features

- SLA rule enforcement (Failure rate, Avg. response time, Response violation rate)
- Real-time SLA check via Jupyter or scheduled job
- Email alerts when violations are detected
- Streamlit dashboard with tables and charts
- SQLite simulation of cloud DB storage
- Customizable input/output paths and thresholds
- Modular structure using utility functions

---

## 🗂 Folder Structure

SLA-Monitoring-System/

│

├── sla_monitor.py # SLA checking logic

├── monitor_sla.py # Scheduler/automation

├── send_email.py # Email alert functionality

├── sla_dashboard.py # Streamlit dashboard UI

├── requirements.txt # Required Python packages

├── README.md # This project description file

│

├── data/

│ └── sample_sla_data.csv # Input service metrics

│

├── utils/

│ └── upload_to_cloud.py # Cloud simulation (optional)

│

├── sla_violations_report.csv # Auto-generated violation report

├── sla_violations.db # SQLite DB to simulate cloud

---

## ⚙️ How It Works

### 1. Check for SLA Violations

```python
from sla_monitor import run_sla_check
run_sla_check()

2. Simulate Cloud DB Upload (Optional)
from utils.upload_to_cloud import upload_to_cloud
upload_to_cloud("sla_violations_report.csv")

3. Send Email Alert (Automatically triggered)
from send_email import send_email_alert
send_email_alert(violation_df)

🔁 Scheduled Monitoring
We can automate the check using the monitor_sla.py script:

python monitor_sla.py


This will run run_sla_check() every 60 seconds using schedule.

📊 Real-Time Dashboard (Streamlit)
Launch the interactive dashboard:
streamlit run sla_dashboard.py


Features:

View violations in table format

Filters by service name and violation type

Auto-refresh and visual insights (bar, pie charts)



✉️ Email Alerts
When violations are detected, an email alert is triggered automatically:

send_email.py:


sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
app_password = "your_app_password"


Use Gmail App Password if 2FA is enabled.

☁️ Simulated Cloud Storage
To simulate uploading violation data to a cloud DB:

from utils.upload_to_cloud import upload_to_cloud
upload_to_cloud("sla_violations_report.csv")


Also stores violations into local SQLite DB:

conn = sqlite3.connect("sla_violations.db")


🧪 Sample Output
Here is an example of a violation report:

service_name	failure_rate	avg_response_time_ms	response_violation_rate
Service A	      0.09	                1600	                    0.02
Service C	      0.15	                1400	                    0.06


✅ Installation
Install all dependencies:





💡 Future Enhancements
I will Add real cloud upload via AWS S3 / Google Drive

I will Add Slack/Discord alerts

Store historical trends and plot time-series graphs

I will Add authentication to dashboard

I will Deploy to cloud (Azure, AWS, etc.)

👨‍💻 Author
Built by Gouthum Kharvi
Email: gouthumkharvi1899@gmail.com
