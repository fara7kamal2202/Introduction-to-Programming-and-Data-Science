# ================================
# Exercise: Write a function add_one(). It takes an integer as argument.
# The function adds 1 to the integer and returns it.
#
# Write another function add_one_to_list(). It takes a list of integers as argument.
# Define a variable new_list in this function.
# Using a for loop, iterate through the argument list.
# Using add_one(), fill new_list with integers from the argument list incremented by 1.
# Print new_list.
#
# Test both functions.
# ================================

# Write your first function here:
def add_one(number):
    return number + 1

# Write your second function here:
def add_one_to_list(numbers):
    new_list = []
    for number in numbers:
        new_list.append(add_one(number))
    print(new_list)

# Test add_one() function (change values to test more):
print("Testing add_one():")
print("add_one(5) =", add_one(5))  # Should return 6
print("add_one(0) =", add_one(0))  # Should return 1
print("add_one(-3) =", add_one(-3))  # Should return -2

print("---")  # Separator for clarity

# Test add_one_to_list() function (change lists to test more):
print("Testing add_one_to_list():")
original_list = [1, 2, 3, 4, 5]  # You can modify this list
add_one_to_list(original_list)

test_list = [10, 20, 30]  # Another test list
add_one_to_list(test_list)
