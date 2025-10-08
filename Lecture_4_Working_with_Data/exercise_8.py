import pandas as pd
import numpy as np

# ================================
# Exercise: Iris Metadata Analysis
# ================================

# Task 1: Read the file 'iris.csv' (or 'iris.xlsx')

df = pd.read_csv('iris.csv')

# ================================
# Task 2: Try out the following functions. What do they output? What do they do?
# Tip: You can also copypaste these lines in the python interpreter
# ================================
# Data Viewing Functions:
# Functions to view and inspect DataFrame or Series objects.
#
# Example:
# head(), tail(), info(), describe()
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

# ================================
# Task 3: Try out the following functions. What do they output? What do they do?
# Tip: You can also copypaste these lines in the python interpreter
# ================================
# Data Selection and Indexing Functions:
# Functions for selecting, filtering, and indexing data within DataFrames and Series.
#
# Example:
# loc[], iloc[], isin()
print(df.loc[0, 0])
print(df.loc[0, 'sepal.length'])
print(df.iloc[0, 0])
print(df['variety'].isin(['Setosa']))

# ================================
# Task 4: Try out the following functions. What do they output? What do they do?
# Tip: You can also copypaste these lines in the python interpreter
# ================================
# Data Aggregation and Calculation Functions:
# Functions for aggregating and calculating statistics on data.
#
# Example:
# sum(), mean(), median(), min(), max()
print(df.sum(numeric_only=True))
print(df.mean(numeric_only=True))
print(df.median(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))

# ================================
# Task 5: Try out the following functions. What do they output? What do they do?
# Tip: You can also copypaste these lines in the python interpreter
# ================================
# Data Cleaning Functions:
# Functions for handling missing values, duplicates, and other data cleaning tasks.
#
# Example:
# dropna(), fillna(), drop_duplicates()
print(df.dropna())
print(df.fillna(0))
print(df.drop_duplicates())

