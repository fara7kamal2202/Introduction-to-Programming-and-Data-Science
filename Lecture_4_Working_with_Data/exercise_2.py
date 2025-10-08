import numpy as np

# ================================
# Exercise: Broadcasting
# ================================

# Task 1: Create a list 'numbers_list' containing numbers 1 to 10.
# Add 1 to each element in numbers_list using a loop.

numbers_list = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
# Note: Think about how you would add 1 to each element in a list
numbers_list_plus_one = [i + 1 for i in numbers_list]
print("List + 1:", numbers_list_plus_one)


# ================================
# Task 2: Create a 1D array 'numbers_array' using NumPy containing numbers 1 to 10.
# Add 1 to each element in numbers_array using broadcasting.
# ================================

numbers_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# Note: Broadcasting makes this much simpler with NumPy
numbers_array_plus_one = numbers_array + 1
print("Array + 1:", numbers_array_plus_one)


# ================================
# Task 3: Broadcasting a 1D array onto rows of a 2D array
# Create a 2D array of shape (3, 4) filled with zeros.
# Create a 1D array containing [1, 2, 3, 4].
# Add the 1D array to each row of the 2D array using broadcasting.
# ================================

# Create a 2D array of zeros with shape (3, 4)
matrix = np.zeros((3, 4))
print("\nOriginal 2D array:")
print(matrix)

# Create a 1D array to broadcast
row_values = np.array([1, 2, 3, 4])
print("\n1D array to broadcast:", row_values)

# Note: Broadcasting adds the 1D array to each row
result_rows = matrix + row_values
print("\nResult after row-wise broadcasting:")
print(result_rows)


# ================================
# Task 4: Broadcasting two 2D arrays onto each other
# Create a 2D array of shape (3, 4) filled with zeros.
# Create a 2D array containing [[10], [20], [30]].
# Add the arrays using broadcasting.
# ================================

# Create a 2D array of zeros with shape (3, 4)
matrix2 = np.zeros((3, 4))
print("\nOriginal 2D array:")
print(matrix2)

# Create a 2D array to add to the first array
matrix3 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
print("\n2D array to add to the first array:", matrix3)

# Add both arrays and see how the broadcasting behaves.
result_matrix = matrix3 + matrix2
print("\nResult after column-wise broadcasting:")
print(result_matrix)


