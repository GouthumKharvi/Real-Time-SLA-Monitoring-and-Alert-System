
import streamlit as st
import pandas as pd

st.title("SLA Violations Dashboard")

# Load SLA violations report
df = pd.read_csv('sla_violations_report.csv')

st.subheader("All SLA Violations")
st.dataframe(df)
