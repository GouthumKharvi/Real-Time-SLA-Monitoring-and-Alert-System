
import pandas as pd

# Define SLA thresholds
FAILURE_RATE_THRESHOLD = 0.05  # 5%
RESPONSE_TIME_THRESHOLD_MS = 2000  # 2 seconds
RESPONSE_VIOLATION_RATE_THRESHOLD = 0.1  # 10%

def run_sla_check(file_path='data/platform_logs.csv'):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Input file not found at: {file_path}")
        return []

    violations = []

    for _, row in df.iterrows():
        if (
            row['failure_rate'] > FAILURE_RATE_THRESHOLD or
            row['avg_response_time_ms'] > RESPONSE_TIME_THRESHOLD_MS or
            row['response_violation_rate'] > RESPONSE_VIOLATION_RATE_THRESHOLD
        ):
            violations.append(row)

    if violations:
        violation_df = pd.DataFrame(violations)
        violation_df.to_csv('sla_violations_report.csv', index=False)
        print("SLA violations found and report saved.")
        return violation_df
    else:
        print("No SLA violations detected.")
        return pd.DataFrame()
