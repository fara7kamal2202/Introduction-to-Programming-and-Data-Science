import pandas as pd
import numpy as np

# ================================
# Exercise: Iris Data Analysis with Pandas and NumPy
# ================================

# Task 1: Read the file 'iris.csv' (or 'iris.xlsx')

iris_df = pd.read_csv('iris.csv')

# ================================
# Task 2: Print the first few rows of the dataset
# ================================

print("First few rows of the dataset:")
print(iris_df.head())

# ================================
# Task 3: Filter the dataset to select only the 'Versicolor' species
# ================================

versicolor_df = iris_df[iris_df["variety"] == "Versicolor"]

# ================================
# Task 4: Convert the filtered dataset into a NumPy array.
# Print the shape of the converted array (versicolor_np). How many rows and columns does it have?
# ================================

versicolor_np = versicolor_df.to_numpy()
print(versicolor_np.shape)

# ================================
# Task 5: Calculate mean and standard deviation of sepal length, sepal width, petal length, and petal width
# ================================

sepal_length_mean = versicolor_df['sepal.length'].mean()
sepal_length_std = versicolor_df["sepal.length"].std()

sepal_width_mean = versicolor_df["sepal.width"].mean()
sepal_width_std = versicolor_df["sepal.width"].std()

petal_length_mean = versicolor_df["petal.length"].mean()
petal_length_std = versicolor_df["petal.length"].std()

petal_width_mean = versicolor_df["petal.width"].mean()
petal_width_std = versicolor_df["petal.width"].std()

print("\nStatistics for 'Versicolor' species:")
print("Mean sepal length:", sepal_length_mean)
print("Standard deviation sepal length:", sepal_length_std)
print("Mean sepal width:", sepal_width_mean)
print("Standard deviation sepal width:", sepal_width_std)
print("Mean petal length:", petal_length_mean)
print("Standard deviation petal length:", petal_length_std)
print("Mean petal width:", petal_width_mean)
print("Standard deviation petal width:", petal_width_std)
