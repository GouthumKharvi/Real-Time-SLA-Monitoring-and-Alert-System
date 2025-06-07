import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# -- Add a bar plot for Failure Rate by Service Name --
st.subheader("Failure Rate by Service")

plt.figure(figsize=(10, 5))
sns.barplot(data=filtered_df, x='service_name', y='failure_rate')
plt.xticks(rotation=45)
plt.ylabel("Failure Rate (%)")
plt.xlabel("Service Name")
plt.title("Failure Rate per Service")

st.pyplot(plt.gcf())

# -- Add a scatter plot for Failure Rate vs Response Violation Rate --
st.subheader("Failure Rate vs Response Violation Rate")

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=filtered_df,
    x='failure_rate',
    y='response_violation_rate',
    hue='service_name',
    palette='Set2',
    s=100,
    alpha=0.7
)
plt.xlabel("Failure Rate (%)")
plt.ylabel("Response Violation Rate (%)")
plt.title("Failure Rate vs Response Violation Rate")
plt.legend(title='Service', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

st.pyplot(plt.gcf())
