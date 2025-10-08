import numpy as np

# ================================
# Exercise: Additional NumPy Concepts
# ================================

# Task 1: Array Concatenation
# Create two arrays: arr1 = [1, 2, 3] and arr2 = [4, 5, 6]
# Concatenate them horizontally

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))
print("Concatenated array:", concatenated)


# ================================
# Task 2: Array Stacking
# Stack arr1 and arr2 vertically to create a 2D array
# ================================

stacked = np.stack((arr1, arr2))
print("Vertically stacked array:")
print(stacked)


# ================================
# Task 3: Array Transpose
# Create a 2x3 matrix and find its transpose
# ================================

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
transposed = np.transpose(matrix)
print("Original matrix:")
print(matrix)
print("Transposed matrix:")
print(transposed)


# ================================
# Task 4: Dot Product
# Calculate the dot product of two vectors: [1, 2, 3] and [4, 5, 6]
# ================================

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
dot_product = np.dot(vector1, vector2)
print("Dot product:", dot_product)


# ================================
# Task 5: Boolean Indexing
# Create an array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use boolean indexing to select only elements greater than 5
# ================================

numbers = np.arange(1, 11)
greater_than_5 = numbers > 5
print("Elements greater than 5:", greater_than_5)


# ================================
# Task 6: Array Sorting
# Create a random array of 10 integers between 1 and 100
# Sort it in ascending order
# ================================

random_array = np.random.randint(1, 101, 10)
print("Original random array:", random_array)
sorted_array = np.sort(random_array)
print("Sorted array:", sorted_array)


# ================================
# Task 7: Unique Values
# Create an array with duplicate values: [1, 2, 2, 3, 3, 3, 4, 5, 5]
# Find the unique values
# ================================

array_with_duplicates = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5])
unique_values = np.unique_values(array_with_duplicates)
print("Unique values:", unique_values)


# ================================
# Task 8: Array Math Operations
# Create an array [1, 4, 9, 16, 25]
# Calculate the square root of each element
# ================================

squares = np.array([1, 4, 9, 16, 25])
square_roots = np.sqrt(squares)
print("Square roots:", square_roots)


# ================================
# Task 9: Cumulative Sum
# Create an array [1, 2, 3, 4, 5]
# Calculate the cumulative sum
# ================================

arr = np.array([1, 2, 3, 4, 5])
cumsum = np.cumsum(arr)
print("Cumulative sum:", cumsum)


# ================================
# Task 10: Where Function
# Create an array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Replace all values less than 5 with 0 and values >= 5 with 1
# ================================

arr = np.arange(1, 11)
binary_array = np.where(arr >= 5, arr, 1)
binary_array = np.where(binary_array < 5, binary_array, 0)
print("Binary array (0 if < 5, 1 if >= 5):", binary_array)
