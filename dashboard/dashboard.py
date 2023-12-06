import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
from plotly.subplots import make_subplots
import streamlit as st
from babel.numbers import format_currency


sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

#hourly status
def create_hourly_stats(df):
    hourly_stats_df = df.groupby('hr')['cnt_hour'].mean().reset_index()
    return hourly_stats_df

#daily status
def create_daily_stats(df):
    daily_stats_df = df.groupby('dteday')['cnt_day'].mean().reset_index()
    return daily_stats_df

#daily status
def create_monthly_stats(df):
    monthly_stats_df = df.groupby('mnth_hour')['cnt_day'].mean().reset_index()
    return monthly_stats_df

# Filter the dataset for each season and calculate aggregate statistics
def create_seasonal_analysis(all_data):
    # Filter the dataset for each season and calculate aggregate statistics
    seasonal_analysis_df = all_data.groupby('season_day').agg({
        'cnt_day': ['count', 'mean', 'std', 'min', 'max']
    }).reset_index()

    # Rename the columns for better readability
    seasonal_analysis_df.columns = ['Season', 'Count', 'Mean', 'Std', 'Min', 'Max']
    return seasonal_analysis_df

def create_rfm_df(df):
    # Calculate Recency, Frequency, and Monetary Value
    current_date = df['dteday'].max()

    # Recency
    recency = df.groupby('registered_hour')['dteday'].max().reset_index()
    recency['recency'] = (current_date - recency['dteday']).dt.days
    recency = recency[['registered_hour', 'recency']]

    # Frequency
    frequency = df.groupby('registered_hour').size().reset_index(name='frequency')

    # Monetary Value
    monetary_value = df.groupby('registered_hour')['cnt_hour'].sum().reset_index(name='monetary_value')

    # Merge the three metrics
    rfm_data = pd.merge(recency, frequency, on='registered_hour')
    rfm_data = pd.merge(rfm_data, monetary_value, on='registered_hour')

    return rfm_data


# Load cleaned data
all_data = pd.read_csv("all_data.csv")

datetime_columns = ["dteday"]  # Assuming 'dteday' is the date column
all_data.sort_values(by="dteday", inplace=True)
all_data.reset_index(inplace=True)

for column in datetime_columns:
    all_data[column] = pd.to_datetime(all_data[column])

# Filter data
min_date = all_data["dteday"].min()
max_date = all_data["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://drive.google.com/file/d/13fzir0sZOlAA8QWRb_yMNWS-hUDXORlg/view?usp=sharing")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_data[(all_data["dteday"] >= str(start_date)) & 
                (all_data["dteday"] <= str(end_date))]

# st.dataframe(main_df)

# # Menyiapkan berbagai dataframe
hourly_stats_df = create_hourly_stats(main_df)
daily_stats_df = create_daily_stats(main_df)
monthly_stats_df = create_monthly_stats(main_df)
seasonal_analysis_df = create_seasonal_analysis(main_df)
rfm_data = create_rfm_df(main_df)


# plot number of daily orders (2021)
st.header('Bike Sharing Dashboard :sparkles:')
# Streamlit app
st.subheader('Hourly Bike Rental Trends')
# hourly Trends
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    hourly_stats_df["hr"], 
    hourly_stats_df["cnt_hour"], 
    marker='o'
)
ax.set_title('Hourly Bike Rental Trend')
ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Average Bike Rentals')
ax.grid(True)

# Daily
# Text between visualizations
st.pyplot(fig)
# Create a figure and axes
fig, ax = plt.subplots(figsize=(14, 6))
st.write("### Daily Bike Rental Trends")
# Plot the daily trend
ax.plot(
    daily_stats_df['dteday'], 
    daily_stats_df['cnt_day'], 
    marker='o'
)
ax.set_title('Daily Bike Rental Trend')
ax.set_xlabel('Date')
ax.set_ylabel('Average Bike Rentals')
ax.tick_params(axis='x', rotation=45)
ax.grid(True)
 # Display the Matplotlib plot in Streamlit
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 6))
st.write("### Monthly Bike Rental Trends")
# Plot the monthly trend
ax.plot(monthly_stats_df['mnth_hour'], monthly_stats_df['cnt_day'], marker='o')
ax.set_title('Monthly Bike Rental Trend')
ax.set_xlabel('Month')
ax.set_ylabel('Average Bike Rentals')
ax.grid(True)
# Display the Matplotlib plot in Streamlit
st.pyplot(fig)

# Set the style of seaborn
sns.set(style="whitegrid")

# Create a bar plot for the seasonal analysis
fig, ax = plt.subplots(figsize=(10, 6))
st.write("### Season and calculate aggregate statistics")
sns.barplot(x='Season', y='Mean', data = seasonal_analysis_df, palette="viridis")
plt.title('Average Bike Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Average Bike Rentals')
st.pyplot(fig)

# Create subplots
# Plot the RFM Analysis
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
st.write("### Top 5 Registered Users Based on RFM Parameters")
# Set colors
colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

    # Plot bar charts
sns.barplot(y="recency", x="registered_hour", data=rfm_data.sort_values(by="recency", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel("Recency")
ax[0].set_xlabel("User Registered Hour")
ax[0].set_title("Top 5 Users by Recency (days)", loc="center", fontsize=12)
ax[0].tick_params(axis='x', labelsize=10)

sns.barplot(y="frequency", x="registered_hour", data=rfm_data.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel("Frequency")
ax[1].set_xlabel("User Registered Hour")
ax[1].set_title("Top 5 Users by Frequency", loc="center", fontsize=12)
ax[1].tick_params(axis='x', labelsize=10)

sns.barplot(y="monetary_value", x="registered_hour", data=rfm_data.sort_values(by="monetary_value", ascending=False).head(5), palette=colors, ax=ax[2])
ax[2].set_ylabel("Monetary Value")
ax[2].set_xlabel("User Registered Hour")
ax[2].set_title("Top 5 Users by Monetary Value", loc="center", fontsize=12)
ax[2].tick_params(axis='x', labelsize=10)

plt.suptitle("Top 5 Registered Users Based on RFM Parameters (registered_hour)", fontsize=14)
st.pyplot(fig)




st.caption('Copyright © yuliaharni 2023')