import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the car sales data
car_sales_df = pd.read_csv('Car_sales.csv')

# Seaborn for better aesthetics
sns.set(style="whitegrid")

# 1. Sales by Manufacturer
plt.figure(figsize=(12, 6))
manufacturer_sales = car_sales_df.groupby("Manufacturer")["Sales_in_thousands"].sum().sort_values(ascending=False)
sns.barplot(x=manufacturer_sales.index, y=manufacturer_sales.values, palette="viridis")
plt.xticks(rotation=90)
plt.title("Total Sales by Manufacturer")
plt.xlabel("Manufacturer")
plt.ylabel("Sales in Thousands")
plt.show()


# 5. Distribution of Vehicle Prices
plt.figure(figsize=(10, 6))
sns.histplot(car_sales_df["Price_in_thousands"].dropna(), bins=20, kde=True, color="skyblue")
plt.title("Distribution of Vehicle Prices")
plt.xlabel("Price in Thousands")
plt.ylabel("Frequency")
plt.show()