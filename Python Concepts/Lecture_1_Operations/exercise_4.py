# ================================
# Exercise: String Operations
# ================================

#NOTE: We are expecting knowledge from section "4. Collections" (i.e. list indexing) here
#NOTE: We are expecting knowledge from section "7. Functions" (i.e. string methods) here

# Given strings
first_name = "John"
last_name = "Doe"
middle_initial = "M"

# Task 1: Concatenate strings to create a full name with middle initial
# Expected output: "John M. Doe"
full_name = f"{first_name} {middle_initial}. {last_name}"

# Task 2: Convert the full name to uppercase
uppercase_name = full_name.upper()

# Task 3: Count the total number of characters (excluding spaces)
# Hint: Use replace() to remove spaces, then len()
char_count = len(full_name.replace(" ", ""))

# Task 4: Create initials from the full name
# Expected output: "JMD"
initials = f"{first_name[0]}{middle_initial}{last_name[0]}"

print(f"Full name: {full_name}")
print(f"Uppercase: {uppercase_name}")
print(f"Character count (no spaces): {char_count}")
print(f"Initials: {initials}")
