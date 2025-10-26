# ================================
# Exercise: Write a function check_value(), which takes a number as an argument.
# Using if / else, the function should print whether the number is bigger, smaller, or equal to 5.
# Test your function with different values.
# ================================

# Write your function here:
def check_value(value):
    number_to_check = 5
    if value == number_to_check:
        verdict = f"{value} is equal to {number_to_check}"
    elif value > number_to_check:
        verdict = f"{value} is bigger than {number_to_check}"
    else:
        verdict = f"{value} is smaller than {number_to_check}"
    print(verdict)


# Test your function with these values (change them to test more):
check_value(3)  # Should print: "3 is smaller than 5"
check_value(5)  # Should print: "5 is equal to 5"
check_value(10)  # Should print: "10 is bigger than 5"