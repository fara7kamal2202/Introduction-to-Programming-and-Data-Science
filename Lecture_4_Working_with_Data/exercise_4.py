import numpy as np

# ================================
# Exercise: Built-in NumPy Functions
# ================================

# Task 1: Create a 1D array with 15 elements using the numpy.arange function.
# Name it my_array

my_array = np.arange(15)
print("Original array:", my_array)


# ================================
# Task 2: Print the index value of the minimum element in my_array
# ================================

min_index = np.argmin(my_array)
print("Index of minimum element:", min_index)


# ================================
# Task 3: Reshape my_array so that it has 3 rows and 5 columns.
# ================================

reshaped_array = np.reshape(my_array, (3, 5))
print("Reshaped array (3x5):")
print(reshaped_array)


# ================================
# Task 4: Print the mean of each row!
# (You can look up online how to do this - hint: use axis argument)
# ================================

row_means = np.mean(reshaped_array, axis=1)
print("Mean of each row:", row_means)


# ================================
# Task 5: Print the max/min of each column!
# (You can look up online how to do this - hint: use axis argument)
# ================================

column_max = np.max(reshaped_array, axis=0)
column_min = np.min(reshaped_array, axis=0)
print("Max of each column:", column_max)
print("Min of each column:", column_min)


# ================================
# Task 6: Create an array of zeros with shape (2, 4)
# ================================

zeros_array = np.zeros((2, 4))
print("\nArray of zeros:")
print(zeros_array)


# ================================
# Task 7: Create an array of ones with shape (3, 3)
# ================================

ones_array = np.ones((3, 3))
print("\nArray of ones:")
print(ones_array)


# ================================
# Task 8: Create a 4x4 identity matrix (diagonal of 1s, rest 0s)
# ================================

identity_matrix = np.identity(4)
print("\n4x4 Identity matrix:")
print(identity_matrix)


# ================================
# Task 9: Generate a random array of shape (2, 3) with values between 0 and 1
# ================================

random_array = np.random.random((2, 3))
print("\nRandom array:")
print(random_array)


# ================================
# Task 10: Use linspace to create an array of 10 evenly spaced values
# between 0 and 5
# ================================

linspace_array = np.linspace(0, 5, 10)
print("\nEvenly spaced values from 0 to 5:")
print(linspace_array)
