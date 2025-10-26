# ================================
# Exercise: Ticket Pricing
# ================================

# Instructions:
# Write a Python program that asks the user for their age and determines the price of a movie ticket based on the following criteria:
#
# If the age is below 12, the ticket costs 5 Euros.
# If the age is between 12 and 65 (inclusive), the ticket costs 10 Euros.
# If the age is above 65, the ticket costs 7 Euros.
# Print out the ticket price.

age = int(input("Enter your age: "))

if age < 12:
    ticket_price = 5
elif age <= 65:
    ticket_price = 10
else:
    ticket_price = 7

print(f"The ticket price is {ticket_price}")
