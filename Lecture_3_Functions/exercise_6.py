# ================================
# Exercise: Write a function print_numbers(), which takes a list of numbers as argument.
# Using a for loop, print each number one by one on a new line.
# Note: print() automatically adds a newline, but you can also use the escape character \n
# Test your function with a list of numbers.
# ================================

# Write your function here:
def print_numbers(number_list):
    for number in number_list:
        print(number)

# Test your function with these lists (change them to test more):
my_numbers = [10, 20, 30, 40, 50]  # You can modify this list
print_numbers(my_numbers)

print("---")  # Separator for clarity

small_list = [1, 2, 3]  # Another test list
print_numbers(small_list)