# ================================
# Exercise: Numeric Precision
# ================================

# Task 1: Large number precision loss
# What happens when we convert very large integers to float and back?

huge_number = 12345678901234567890
huge_as_float = float(huge_number)
back_to_int = int(huge_as_float)

print("=== Large Number Precision ===")
print(f"Original: {huge_number}")
print(f"As float: {huge_as_float}")
print(f"Back to int: {back_to_int}")
print(f"Lost precision: {huge_number - back_to_int}")

