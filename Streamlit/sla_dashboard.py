import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="SLA Monitoring Dashboard", layout="wide")
st.title("📊 SLA Violations Dashboard")

@st.cache_data(ttl=60)
def load_data():
    return pd.read_csv("data/sample_sla_data.csv")

# Load data
df = load_data()

# Convert 'date' column to datetime
df["date"] = pd.to_datetime(df["date"])

# Filters
st.sidebar.header("🔎 Filters")
service_filter = st.sidebar.multiselect(
    "Service Name", options=df["service_name"].unique(), default=df["service_name"].unique()
)
violation_filter = st.sidebar.multiselect(
    "Violation Type", options=df["violation_type"].unique(), default=df["violation_type"].unique()
)
date_range = st.sidebar.date_input(
    "Date Range", [df["date"].min().date(), df["date"].max().date()]
)

# Apply filters
filtered_df = df[
    (df["service_name"].isin(service_filter)) &
    (df["violation_type"].isin(violation_filter)) &
    (df["date"].dt.date >= date_range[0]) &
    (df["date"].dt.date <= date_range[1])
]

# Display filtered data
st.subheader("📋 Filtered SLA Violations")
st.dataframe(filtered_df, use_container_width=True)

# Bar chart: Violations per service
st.subheader("📉 Violations by Service")
service_counts = filtered_df["service_name"].value_counts()
st.bar_chart(service_counts)

# Pie chart: Violation type distribution
st.subheader("📌 Violation Types Distribution")
violation_counts = filtered_df["violation_type"].value_counts()
fig, ax = plt.subplots()
ax.pie(violation_counts, labels=violation_counts.index, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)
