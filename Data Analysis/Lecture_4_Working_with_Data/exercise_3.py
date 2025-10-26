import numpy as np

# ================================
# Exercise: Manipulating NumPy Arrays
# ================================

# Task 1: Create a 3x3 NumPy array named 'my_array' with the following elements:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

my_array = np.matrix([[1,2,3],[4,5,6],[7,8,9]])


# ================================
# Task 2: Access and print the element at row index 1 and column index 2.
# ================================

element = my_array[1,2]
print("Element at row 1, column 2:", element)


# ================================
# Task 3: Access and print the entire second row of my_array
# ================================

second_row = my_array[1, :]
print("Second row:", second_row)


# ================================
# Task 4: Access and print the entire third column of my_array
# ================================

third_column = my_array[:, 2]
print("Third column:", third_column)


# ================================
# Task 5: Slice and print a 2x2 sub-array from my_array containing
# elements from the first two rows and first two columns.
# ================================

sub_array = my_array[:2, :2]
print("2x2 sub-array:")
print(sub_array)


# ================================
# Task 6: Use negative indexing to access and print the element at
# row index -1 (last row) and column index -2 (second-to-last column).
# ================================

negative_index_element = my_array[-1, -2]
print("Element at row -1, column -2:", negative_index_element)


# ================================
# Task 7: Multiply all the elements in the array by 3
# ================================

my_array_times_3 = my_array * 3
print("Array multiplied by 3:")
print(my_array_times_3)


# ================================
# Task 8: Print the maximum, minimum, and mean of the array
# (use the built-in functions)
# ================================

array_max = np.max(my_array)
array_min = np.min(my_array)
array_mean = np.mean(my_array)

print("\nArray statistics:")
print("Maximum:", array_max)
print("Minimum:", array_min)
print("Mean:", array_mean)
