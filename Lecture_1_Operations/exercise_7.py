# ================================
# Exercise: Modulo and Integer Division
# ================================

# Task: Work with time conversion and modulo operations

total_seconds = 7265  # Total time in seconds

# Task 1: Convert total seconds to hours, minutes, and seconds
# Use integer division (//) and modulo (%)
hours = 7265 // 3600
remaining_after_hours = 7265 % 3600 #remaining seconds after complete hours were removed
minutes = remaining_after_hours // 60
seconds = remaining_after_hours % 60

# Task 2: Check if a number is even or odd using modulo
number = 42
is_even = 42 % 2 == 0  # True if even, False if odd

# Task 3: Calculate the day of week
# Given: Day 0 is Monday, Day 6 is Sunday
# If today is Wednesday (day 2) and we add 10 days, what day will it be?
today = 2  # Wednesday
days_to_add = 10
future_day = (today + days_to_add) % 7  # Use modulo to wrap around the week

# Task 4: Distribute items evenly
# You have 100 candies to distribute among 7 children
candies = 100
children = 7
candies_per_child = 100 // 7  # Each child gets this many
leftover_candies = 100 % 7  # Remaining candies after equal distribution

print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")
print(f"Is {number} even? {is_even}")
print(f"Day after {days_to_add} days from Wednesday: Day {future_day}")
print(f"Each child gets {candies_per_child} candies, with {leftover_candies} leftover")
