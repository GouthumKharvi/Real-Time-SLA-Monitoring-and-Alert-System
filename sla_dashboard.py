# Path where you want to save the file
file_path = r"C:\Users\Gouthum\Downloads\DE\sla_dashboard.py"

# The Streamlit dashboard code as a multi-line string
dashboard_code = """
import streamlit as st
import pandas as pd

st.title("SLA Violations Dashboard")

# Load SLA violations report
df = pd.read_csv('sla_violations_report.csv')

st.subheader("All SLA Violations")
st.dataframe(df)
"""

# Write the code string to the file
with open(file_path, 'w') as file:
    file.write(dashboard_code)

print(f"File saved successfully at: {file_path}")
