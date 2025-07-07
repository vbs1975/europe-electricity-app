import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the filtered CSV
df = pd.read_csv("selected_countries.csv")

# Convert 'date' column to datetime format for accurate plotting
df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(14, 7))
sns.set(style="whitegrid")

# Plot points for each country with labels
for country in df['country'].unique():
    country_data = df[df['country'] == country]
    plt.scatter(country_data['date'], country_data['price'], label=country, s=50)

    # Add country name labels on each point
    for _, row in country_data.iterrows():
        plt.text(row['date'], row['price'], country, fontsize=7, alpha=0.7, rotation=45)

plt.title("Monthly Energy Prices for Selected Countries")
plt.xlabel("Date")
plt.ylabel("Price (EUR/MWhe)")
plt.legend()
plt.tight_layout()
plt.savefig("energy_prices_selected_countries.png", dpi=300)
plt.show()

