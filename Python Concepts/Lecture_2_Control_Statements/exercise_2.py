# ===========================================
# Exercise: Positive/Negative/Zero Checker
# ===========================================

# Instructions:
# Write a Python program that takes a number as input and prints out whether it's positive, negative, or zero.
number = float(input("Enter a number: "))
if number == 0:
    print("The number is 0")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is negative")
...
