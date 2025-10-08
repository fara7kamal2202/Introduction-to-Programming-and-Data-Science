# ================================
# Exercise: Calculate the factorial of a given number using a while loop
# ================================


# Hint: The factorial of 4 is 4! = 4 * 3 * 2 * 1
number = int(input("Enter a number: "))

factorial = 1

# Insert while loop here!
while number > 1:
    factorial *= number
    number -= 1

print("Factorial:", factorial)