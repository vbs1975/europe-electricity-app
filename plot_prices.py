import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("avg_prices_per_year.csv")
df["year"] = df["year"].astype(int)

sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

sns.scatterplot(
    data=df,
    x="year",
    y="avg_price",
    hue="country",
    palette="tab10",
    s=100,
    legend=False
)

for _, row in df.iterrows():
    plt.text(row["year"] + 0.1, row["avg_price"], row["country"], fontsize=8, alpha=0.7)

plt.title("Average Electricity Prices per Country per Year")
plt.xlabel("Year")
plt.ylabel("Average Price (EUR/MWhe)")
plt.tight_layout()

plt.savefig("avg_prices_plot.png", dpi=300)  # Save as PNG
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the cleaned, aggregated data
df = pd.read_csv("avg_prices_per_year.csv")

# Convert year to integer if it's not already
df["year"] = df["year"].astype(int)

# Set seaborn style
sns.set(style="whitegrid")

# Create the scatter plot
plt.figure(figsize=(12, 6))
scatter = sns.scatterplot(data=df, x="year", y="avg_price", hue="country", palette="tab10", s=100, legend=False)

# Annotate each point with country name
for _, row in df.iterrows():
    plt.text(row["year"] + 0.05, row["avg_price"], row["country"], fontsize=8, alpha=0.7)

# Labels and title
plt.title("Average Electricity Prices per Country per Year")
plt.xlabel("Year")
plt.ylabel("Average Price (EUR/MWhe)")
plt.tight_layout()

# Show the plot
plt.show()

