import pprint

# ================================
# Exercise: Combining Different Data Types
# ================================

# Task: Create a personal info system using different collection types

# 1. Create basic variables
name = "Farah"
age = 25
height = 1.68

# 2. Create a list of hobbies (at least 3, string type)
hobbies = ["Reading", "Traveling", "Painting", "Running"]

# 3. Create a set of friends' names (at least 3, string type)
friends = {"X", "Y", "Z"}

# 4. Create a dictionary combining all information
personal_info = {
    "name": name,
    "age": age,
    "height": height,
    "hobbies": hobbies,
    "friends": friends
}

# 5. Print the complete personal information
print("Personal Information:")
print(personal_info)

# 6. Access and print specific information (your choice of key)
print(f"\nName: {personal_info["name"]}")
print(f"Number of hobbies: {len(personal_info["hobbies"])}")
print(f"Number of friends: {len(personal_info["friends"])}")

print(personal_info)
pprint.pprint(personal_info)

# 7. (BONUS) Search the internet for the package "pprint" and use it to print the personal information in a more readable format
# You will need to install the package and include it to use it