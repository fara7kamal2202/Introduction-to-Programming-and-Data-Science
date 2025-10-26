# ================================
# Exercise 1b: Handle Runtime Errors
# ================================

# The code below will cause runtime errors. Add try-except blocks to handle them gracefully.

# Runtime Error 1: Division by zero
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("division cannot be zero")

# Test with division by zero
print(divide_numbers(10, 0))

# Runtime Error 2: Index out of range
my_list = [1, 2, 3]
#print(my_list[5])  # This will cause an IndexError
print(my_list[2])  # This will cause an IndexError

# Runtime Error 3: Type error
def add_values(x, y):
    try:
        if type(x) == int or type(y) == int or type(x) == float or type(y) == float:
            return x + y
    except TypeError as e:
        print(e)

# This will cause a TypeError
result = add_values("5", 10)
print(f"Result: {result}")
