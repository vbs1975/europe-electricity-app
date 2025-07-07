import pandas as pd

# Step 1: Load the CSV file
file_path = "european_wholesale_electricity_price_data_monthly.csv"
df = pd.read_csv(file_path)

# Step 2: Print column names (for confirmation)
print("Columns available in the CSV:")
print(df.columns)

# Step 3: Define correct column names
price_column = 'Price (EUR/MWhe)'
country_column = 'Country'
date_column = 'Date'

# Step 4: Calculate average price (optional)
average_price = df[price_column].mean()
print(f"\nAverage price: {average_price:.2f} EUR/MWhe")

# Step 5: Convert Date column to datetime
df[date_column] = pd.to_datetime(df[date_column])

# Step 6: Filter out all rows where year == 2022 (keep everything NOT in 2022)
df_not_2022 = df[df[date_column].dt.year != 2022]

# Step 7: Sort by price descending and pick top 50 rows
top_50_not_2022 = df_not_2022.sort_values(by=price_column, ascending=False).head(50)

# Step 8: Select relevant columns
selected_columns = [country_column, date_column, price_column]
top_50_not_2022_data = top_50_not_2022[selected_columns]

# Step 9: Print top 50 highest price entries NOT in 2022
print("\nTop 50 highest price entries NOT in 2022:")
print(top_50_not_2022_data)

# Step 10: Save to CSV
output_file = "top_50_high_price_entries_not_2022.csv"
top_50_not_2022_data.to_csv(output_file, index=False)
print(f"\nTop 50 data NOT in 2022 saved to: {output_file}")
