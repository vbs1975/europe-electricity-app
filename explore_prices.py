import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load CSV
file_path = "european_wholesale_electricity_price_data_monthly.csv"
df = pd.read_csv(file_path)

# Step 2: Convert date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Print basic info
print("\nColumn names:")
print(df.columns)
print("\nSample data:")
print(df.head())

# Step 4: Average price per country
country_avg = df.groupby('Country')['Price (EUR/MWhe)'].mean().sort_values()
print("\nAverage price per country:")
print(country_avg)

# Step 5: Line plot – average price over time
monthly_avg = df.groupby('Date')['Price (EUR/MWhe)'].mean()
monthly_avg.plot(title="Average Electricity Price Over Time", figsize=(10,5))
plt.ylabel("EUR/MWhe")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_avg_plot.png")
plt.show()

# Step 6: Bar chart – average price per country
country_avg.plot(kind='barh', title="Average Price per Country", figsize=(10,8))
plt.xlabel("EUR/MWhe")
plt.tight_layout()
plt.savefig("country_avg_bar.png")
plt.show()

# Step 7: Heatmap – price by country and month
df['YearMonth'] = df['Date'].dt.to_period('M')
heatmap_data = df.pivot_table(values='Price (EUR/MWhe)', index='Country', columns='YearMonth')
plt.figure(figsize=(14, 8))
sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=0.2)
plt.title("Monthly Electricity Prices by Country")
plt.tight_layout()
plt.savefig("price_heatmap.png")
plt.show()

# Step 8: Export summary data to Excel
summary = df.groupby('Country')['Price (EUR/MWhe)'].describe()
summary.to_excel("price_summary.xlsx")
print("\nSummary saved to: price_summary.xlsx")
