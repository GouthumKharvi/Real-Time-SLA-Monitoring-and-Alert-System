import streamlit as st
import pandas as pd

st.title("SLA Violations Dashboard")

# Load SLA violations report
df = pd.read_csv('sla_violations_report.csv')

# Filter by service name dropdown
service_names = ['All'] + df['service_name'].unique().tolist()
selected_service = st.selectbox("Filter by Service", service_names)

filtered_df = df.copy()

if selected_service != 'All':
    filtered_df = filtered_df[filtered_df['service_name'] == selected_service]

# Filter by minimum failure rate slider
min_failure_rate = st.slider(
    "Minimum Failure Rate (%)",
    min_value=0.0,
    max_value=float(df['failure_rate'].max()),
    value=0.0
)
filtered_df = filtered_df[filtered_df['failure_rate'] >= min_failure_rate]

# Filter by minimum response violation rate slider
min_response_violation = st.slider(
    "Minimum Response Violation Rate (%)",
    min_value=0.0,
    max_value=float(filtered_df['response_violation_rate'].max()),
    value=0.0
)
filtered_df = filtered_df[filtered_df['response_violation_rate'] >= min_response_violation]

st.subheader("Filtered SLA Violations")
st.dataframe(filtered_df.reset_index(drop=True))
