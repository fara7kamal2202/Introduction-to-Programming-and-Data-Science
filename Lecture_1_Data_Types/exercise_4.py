# ================================
# Exercise: String to Boolean and None Conversions
# ================================

# Task 1: String to boolean conversions
# Try to predict which of these are True when converted to bool!

empty_string = ""
space_string = " "
false_string = "False"
zero_string = "0"

# Which of these are True when converted to bool?
print(f"bool('') = {bool(empty_string)}")           # Your guess: ... False
print(f"bool(' ') = {bool(space_string)}")          # Your guess: ... True
print(f"bool('False') = {bool(false_string)}")     # Your guess: ... True
print(f"bool('0') = {bool(zero_string)}")           # Your guess: ... True

# Task 2: None conversions
# What happens when we convert None?

none_value = None
none_as_str = str(none_value)      # Your guess: ... "None"
none_as_bool = bool(none_value)    # Your guess: ... False

print(f"\nNone as string: '{none_as_str}' (length: {len(none_as_str)})")
print(f"None as bool: {none_as_bool}")
