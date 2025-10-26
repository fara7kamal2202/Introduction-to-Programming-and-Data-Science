# =================================================
# Exercise: Dictionaries
# =================================================

# Create a dictionary called squares, where you map numbers to their squares.
# For example: 1 maps to 1, 2 maps to 4, 3 maps to 9, etc.
# Do this for the numbers 1-5.
squares = {1: 1,
           2: 4,
           3: 9,
           4: 16,
           5: 25
           }
...

# Accessing the dictionary, save the square of 3 to the variable sq_3. Print it.
sq_3 = squares[3]
print(f"Square 3: {sq_3}")
...

# Add an entry for the number 6 to the dictionary. Print the dictionary.
squares.update({6: 36})
...

# Change the square value of the number 3 to 10. Print the dictisonary.
squares[3] = 10
print(f"Square updated 3: {squares}")
...

# Delete the entry for the number 3 from the dictionary. Print the dictionary.
squares.pop(3)
print(f"Square removed 3: {squares}")
...

# Save all the keys of the dictionary to a variable d_keys. Print it.
d_keys = squares.keys()
print(f"Keys: {d_keys}")
# Save all the values of the dictionary to a variable d_values. Print it.
d_values = squares.values()
print(f"Values: {d_values}")
# Search on the internet how to solve this task.
...