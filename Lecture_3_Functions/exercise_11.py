# ================================
# Exercise: Create a function named 'greet' that takes one parameter/argument 'greeting' and prints it.
# Set the default value of 'greeting' to "Howdy!".
# Use the internet to learn about default parameter values in python: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
# Call the function once without giving any arguments.
# Call it once with passing a greeting of your choice.
# ================================

# Write your function here (hint: def greet(greeting=...)):
def greet(greeting = "Howdy"):
    print(greeting)


# Call the function without arguments (should use default "Howdy!"):
greet()

# Call the function with your own greeting:
greet("Well hello there")  # You can change this greeting

# Try more greetings (optional):
greet("Good morning!")
greet("Hi there!")
