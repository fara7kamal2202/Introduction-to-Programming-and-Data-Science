import pandas as pd
import numpy as np

# ================================
# Exercise: Introduction to Pandas DataFrames
# ================================

# Task 1: Create a simple DataFrame from a dictionary
# Create a DataFrame with columns: 'Name', 'Age', 'City'
# Include at least 4 rows of data

data = {
    'Name': ["Jesse", "Gomez", 'Raven'],
    'Age': [43, 29, 34],
    'City': ["NYC", "Cairo", "Milan"]
}
df = pd.DataFrame(data)
print("DataFrame from dictionary:")
print(df)


# ================================
# Task 2: Create a DataFrame from a list of lists
# Create the same DataFrame using a list of lists approach
# ================================

data_list = [
    ["Jesse", 43, "NYC"],  # First person
    ["Gomez", 29, "Cairo"],  # Second person
    # Add more rows
]
columns = ["Name", "Age", "City"]
df2 = pd.DataFrame(data_list, columns=columns)
print("\nDataFrame from list of lists:")
print(df2)


# ================================
# Task 3: Display basic information about the DataFrame
# ================================

print("\nDataFrame shape (rows, columns):", df2.shape)
print("Column names:", df2.columns)
print("Data types:", df2.dtypes)


# ================================
# Task 4: Access a single column
# Print the 'Name' column
# ================================

names_column = df2["Name"]
print("\nNames column:")
print(names_column)


# ================================
# Task 5: Access multiple columns
# Select and print only 'Name' and 'Age' columns
# ================================

subset = df2[["Age", "City"]]
print("\nName and Age columns:")
print(subset)


# ================================
# Task 6: Access a single row by index
# Print the first row (index 0)
# ================================

first_row = df2.iloc[0]
print("\nFirst row:")
print(first_row)


# ================================
# Task 7: Add a new column
# Add a 'Salary' column with some values
# ================================

df['Salary'] = [1000, 2000, 5000]
print("\nDataFrame with Salary column:")
print(df)


# ================================
# Task 8: Basic statistics
# Calculate and print basic statistics for numerical columns
# ================================

stats = df2.describe()
print("\nBasic statistics:")
print(stats)


# ================================
# Task 9: Create a Series
# Create a pandas Series with some numbers and custom index
# ================================

series = pd.Series([1, 2, 3, 4], index=["x", "y", "z", "w"])
print("\nPandas Series:")
print(series)


# ================================
# Task 10: Convert Series to DataFrame
# Convert the Series to a DataFrame with a column name 'Values'
# ================================

series_df = series.to_frame('Values')
print("\nSeries converted to DataFrame:")
print(series_df)
