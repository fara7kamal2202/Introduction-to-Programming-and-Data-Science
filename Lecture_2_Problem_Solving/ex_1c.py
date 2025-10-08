# ================================
# Exercise 1c: Fix Logic Errors
# ================================

# The code below runs without errors but produces wrong results. Fix the logic!

# Logic Error 1: Wrong operator
def is_even(number):
    # Should return True if number is even
    return number % 2 == 0 # This logic is wrong!

print(f"Is 4 even? {is_even(4)}")  # Should print True

# Logic Error 2: Off-by-one error
def count_to_ten():
    # Should print numbers 1 through 10
    #for i in range(0, 10):  # This doesn't include 10!
    for i in range(0, 11):
        print(i)

count_to_ten()

# Logic Error 3: Wrong variable usage
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    #average = total / total  # Wrong variable used!
    average = total / count
    return average

test_numbers = [10, 20, 30]
print(f"Average: {calculate_average(test_numbers)}")  # Should be 20.0
