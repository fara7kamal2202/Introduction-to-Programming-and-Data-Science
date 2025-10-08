# ================================
# Challenge Exercise: Advanced Functions
# ================================
from numpy.ma.extras import average


# Challenge 1: Recursive Functions
# Write a recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    """
    Calculate the nth Fibonacci number recursively.
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    fib_0 = 0
    fib_1 = 1
    if n == 0:
        return fib_0
    elif n == 1:
        return fib_1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test your function
print(f"Fibonacci(10) = {fibonacci(10)}")  # Should be 55


# ================================
# Challenge 2: Higher-Order Functions
# ================================
# Create a function that returns another function

def create_multiplier(factor):
    """
    Create and return a function that multiplies by the given factor.
    """

    def multiplier(x):
        return x * factor

    return multiplier


# Test it
double = create_multiplier(2)
triple = create_multiplier(3)
print(f"double(5) = {double(5)}")  # Should be 10
print(f"triple(5) = {triple(5)}")  # Should be 15


# ================================
# Challenge 3: Function with Variable Arguments
# ================================
# Create a function that can accept any number of arguments

def calculate_statistics(*numbers):
    """
    Calculate min, max, sum, and average of any number of arguments.
    Return a dictionary with the results.
    """
    if not numbers:
        return {"error": "No numbers provided"}

    result = {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "count": len(numbers),
    }
    return result


# Test with different numbers of arguments
print(calculate_statistics(1, 2, 3, 4, 5))
print(calculate_statistics(10, 20))
print(calculate_statistics(7))

# ================================
# Challenge 4: Decorator Function
# ================================
# Create a decorator that measures function execution time

import time


def time_it(func):
    """
    Decorator that measures and prints the execution time of a function.
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)   # Call the original function
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result

    return wrapper


# Use the decorator
@time_it
def slow_function(n):
    """Simulate a slow function"""
    total = 0
    for i in range(n):
        total += i
    return total


# Test the decorated function
result = slow_function(1000000)
