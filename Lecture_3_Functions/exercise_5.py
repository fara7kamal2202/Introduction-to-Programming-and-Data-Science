# ================================
# Exercise: Write a function check_length(), which takes a string as an argument.
# Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.
# Test your function with different strings.
# ================================

# Write your function here:
def check_length(input):
    wanted_length = 10
    if len(input) == wanted_length:
        print("it's equal to 10")
    elif len(input) < wanted_length:
        print("it's smaller than 10")
    else:
        print("it's bigger than 10")

# Test your function with these strings (change them to test more):
check_length("Hello")  # 5 characters - should print it's smaller than 10
check_length("Python Programming")  # 18 characters - should print it's bigger than 10
check_length("Exactly10!")  # 10 characters - should print it's equal to 10