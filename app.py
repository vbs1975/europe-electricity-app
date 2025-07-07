import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
@st.cache_data
def load_data():
    df = pd.read_csv("european_wholesale_electricity_price_data_monthly.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

st.title("🔌 European Electricity Price Explorer")

# Sidebar filters
st.sidebar.header("📊 Filter the Data")

# Country selection
countries = df['Country'].unique()
selected_countries = st.sidebar.multiselect("Select countries", countries, default=list(countries))

# Date range selection
min_date = df['Date'].min()
max_date = df['Date'].max()
start_date, end_date = st.sidebar.date_input("Select date range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Filter data
filtered = df[
    (df['Country'].isin(selected_countries)) &
    (df['Date'] >= pd.to_datetime(start_date)) &
    (df['Date'] <= pd.to_datetime(end_date))
]

st.markdown(f"### Showing data from {start_date} to {end_date} for {len(selected_countries)} country/countries")

# Line chart
if not filtered.empty:
    st.subheader("📈 Electricity Prices Over Time")
    fig, ax = plt.subplots(figsize=(10, 5))
    for country in selected_countries:
        subset = filtered[filtered['Country'] == country]
        ax.plot(subset['Date'], subset['Price (EUR/MWhe)'], label=country)
    ax.legend()
    ax.set_ylabel("Price (EUR/MWhe)")
    ax.set_title("Electricity Prices")
    ax.grid(True)
    st.pyplot(fig)
else:
    st.warning("No data available for selected filters.")

# Country-level stats
st.subheader("📉 Average Price by Country (filtered)")
avg_price = filtered.groupby('Country')['Price (EUR/MWhe)'].mean().sort_values()
st.dataframe(avg_price)

# Heatmap
st.subheader("🌡️ Heatmap of Prices by Month")
filtered['YearMonth'] = filtered['Date'].dt.to_period('M')
pivot = filtered.pivot_table(values='Price (EUR/MWhe)', index='Country', columns='YearMonth')

fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(pivot, cmap="YlOrRd", linewidths=0.1, ax=ax)
st.pyplot(fig)
