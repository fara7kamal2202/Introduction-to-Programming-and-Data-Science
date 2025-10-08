# ================================
# Exercise: Basic Type Conversions
# ================================

# Task 1: Float to int truncation
# Try to predict the output BEFORE running the code!

# === Example 1: Float to int truncation ===
positive_float = 5.9
negative_float = -5.9
# Predict the results:
positive_int = int(positive_float)  # Your guess: ... 5
negative_int = int(negative_float)  # Your guess: ... -5
print(f"5.9 becomes {positive_int}, -5.9 becomes {negative_int}")

# === Example 2: Boolean conversions ===
true_value = True
false_value = False
# What do these become?
true_as_int = int(true_value)      # Your guess: ... 1
false_as_int = int(false_value)    # Your guess: ... 0
true_as_str = str(true_value)      # Your guess: ... "True"
print(f"True as int: {true_as_int}")
print(f"False as int: {false_as_int}")
print(f"True as string: '{true_as_str}'")

# Now try arithmetic with booleans:
result = true_value + true_value + false_value  # Your guess: ... 2
print(f"True + True + False = {result}")
