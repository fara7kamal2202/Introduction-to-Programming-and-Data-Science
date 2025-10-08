# ================================
# Exercise: Modifying Collections
# ================================

# Start with this personal info dictionary
personal_info = {
    "name": "John",
    "age": 25,
    "height": 1.75,
    "hobbies": ["reading", "gaming", "cooking"],
    "friends": {"Alice", "Bob", "Charlie"}
}

print("Initial Personal Information:")
print(personal_info)

# Task 1: Add a new key-value pair for "city"
personal_info["city"] = "Cairo"

# Task 2: Update the age (birthday happened!)
personal_info["age"] = 26

print("\nUpdated Personal Information:")
print(personal_info)

# Task 3: Add a new hobby to the hobbies list
# Remember: hobbies is a list inside the dictionary
personal_info["hobbies"].append("Fitnessstudio") # Add a new hobby

print("\nUpdated Hobbies:")
print(personal_info["hobbies"])

# Task 4: Add a new friend to the friends set
# Remember: friends is a set inside the dictionary
personal_info["friends"].add("H")  # Add a new friend

print("\nUpdated Friends:")
print(personal_info["friends"])

# Task 5: Remove the first hobby from the list
removed_hobby = personal_info["hobbies"].pop(0)  # Remove and save the first hobby
print(f"\nRemoved hobby: {removed_hobby}")
print(f"Remaining hobbies: {personal_info['hobbies']}")

# Task 6: Check if a specific friend is in the set
friend_to_check = "Alice"
if friend_to_check in personal_info["friends"]: # Note: we use the "in" operator to check if a element is in a enumerable (e.g. list, set, etc.)
    print(f"\n{friend_to_check} is in your friends list!")
else:
    print(f"\n{friend_to_check} is not in your friends list.")
