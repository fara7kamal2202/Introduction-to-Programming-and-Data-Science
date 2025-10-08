# ================================
# Exercise: Create a function named 'fahrenheit_to_celsius' that takes one parameter 'fahrenheit'
# and returns the equivalent temperature in Celsius.
# Formula: celsius = (fahrenheit - 32) * 5/9
# Call the function with a Fahrenheit temperature and print the result.
# ================================

# Write your function here:
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Initial temperature value (you can change this to test):
fahrenheit = 86  # This should convert to 30.0 Celsius
# Call your function and print the result:
new_temp = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is equal to {new_temp}°C")

# Test with more values (you can add more):
print(f"32°F is equal to {fahrenheit_to_celsius(32)}°C")  # Should be 0.0
print(f"212°F is equal to {fahrenheit_to_celsius(212)}°C")  # Should be 100.0
