# ================================
# Exercise: Collections and Special Floats
# ================================

# NOTE: Converting types ("casting") is introduced in Section "4. Collections" ("Working with sets")

# Task 1: Collections to string conversions
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
list_as_str = str(my_list)     # Your guess: "123" or "[1, 2, 3]"? "[1, 2, 3]"
tuple_as_str = str(my_tuple)   # Your guess: "456" or "(4, 5, 6)"? "(4, 5, 6)"
print("=== Collections to String ===")
print(f"List as string: {list_as_str}")
print(f"Tuple as string: {tuple_as_str}")


# Task 2: Special float conversions
# Python recognizes special float strings
print("\n=== Special Float Values ===")
inf_str = "inf"
as_float = float(inf_str)  # Creates actual infinity!
print(f"'{inf_str}' as float: {as_float}")
print(f"Is it really infinity? {as_float > 999999999}")

# Also works with:
print(f"float('-inf') = {float('-inf')}")  # Negative infinity
print(f"float('nan') = {float('nan')}")    # Not a Number

