import numpy as np

# ================================
# Exercise: NumPy Indexing
# ================================

# Task 1: Create a 1D array named 'numbers' containing integers from 1 to 10.
# Print the 4th element of the array.

numbers = np.array([1,2,3,4,5,6,7,8,9,10])
print(f"4th element: {numbers[3]}")


# ================================
# Task 2: Create a 2D array named 'matrix' with 3 rows and 3 columns.
# You can initialize it with any values you prefer.
# ================================

matrix = np.matrix([[1,2,3],[4,5,6],[7,8,9]])


# ================================
# Task 3: Print the element located in the 2nd row and 3rd column of matrix.
# ================================

print(f"Element at 2nd row, 3rd column: {matrix[1, 2]}")


# ================================
# Task 4: Change the value of the element at the 1st row and 2nd column
# of the matrix to 99.
# Print the entire matrix to verify the changes.
# ================================

matrix[0, 1] = 99
print("Matrix after modification:")
print(matrix)


# ================================
# Task 5: Slice the first 2 elements from "numbers" array and print the result.
# ================================

first_two = matrix[1:2]
print(f"First 2 elements: {first_two}")

# ================================
# Task 6: Slice the last 2 rows from matrix array and print the result.
# ================================

last_two_rows = matrix[1:3, :]
print("Last 2 rows:")
print(last_two_rows)
