# ================================
# Exercise: You have the following code written in your program.
# You realize that you need to re-use it a bit later in the program again.
# So, you decide to put the piece of code into a function.
# ================================

# Piece of code to be wrapped into a function
def sum_list(number_list):
    total = 0
    for num in number_list:
        total += num
    print("Sum of numbers:", total)

# Hint: your function should take the "number_list" as an argument.
# Now wrap the above code into a function called sum_list():


# Test your function with these lists (you can modify them):
sum_list([1, 2, 3, 4, 5])  # Should print: Sum of numbers: 15
sum_list([10, 20, 30])  # Should print: Sum of numbers: 60
sum_list([100, 200])  # Should print: Sum of numbers: 300
