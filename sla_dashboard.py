
dashboard_code = '''import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("SLA Violations Dashboard")

@st.cache_data(ttl=60)
def load_data():
    return pd.read_csv('data/sample_sla_data.csv')

# Load data
df = load_data()

# Filters
service_filter = st.multiselect("Filter by Service Name", options=df['service_name'].unique(), default=df['service_name'].unique())
date_range = st.date_input("Select Date Range", [df['date'].min(), df['date'].max()])
violation_types = st.multiselect("Filter by Violation Type", options=df['violation_type'].unique(), default=df['violation_type'].unique())

# Filter data
filtered_df = df[
    (df['service_name'].isin(service_filter)) &
    (df['violation_type'].isin(violation_types)) &
    (df['date'] >= pd.to_datetime(date_range[0])) &
    (df['date'] <= pd.to_datetime(date_range[1]))
]

st.subheader("Filtered SLA Violations")
st.dataframe(filtered_df)

# Bar Chart: Violations by Service
st.subheader("Violation Counts by Service")
service_counts = filtered_df['service_name'].value_counts()
st.bar_chart(service_counts)

# Pie Chart: Violation Type Distribution
st.subheader("Violation Types Distribution")
violation_counts = filtered_df['violation_type'].value_counts()

fig, ax = plt.subplots()
ax.pie(violation_counts, labels=violation_counts.index, autopct='%1.1f%%')
st.pyplot(fig)
'''

# Save to file
with open("C:/Users/Gouthum/Downloads/DE/sla_dashboard.py", "w", encoding="utf-8") as f:
    f.write(dashboard_code)

print("✅ Streamlit dashboard code saved as 'sla_dashboard.py'.")
