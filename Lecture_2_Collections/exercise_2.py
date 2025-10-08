# =================================================
# Exercise: Lists and Sets
# =================================================

# Create a list containing duplicate numbers. Print the list.
list_duplicates = [1, 2, 3, 5, 1, 2, 4, 6, 2, 5]
print(f"List with duplicate elements: {list_duplicates}")
...

# Use set() to get rid of the duplicates. Print the result again.
set_no_duplicates = set(list_duplicates)
print(f"Set with no duplicate elements: {set_no_duplicates}")
...

# Add the number 7 to your new set.
set_no_duplicates.add(7)
print(f"Set, Added 7: {set_no_duplicates}")
...

# Remove the number 7 again.
set_no_duplicates.remove(7)
print(f"Set, Removed 7: {set_no_duplicates}")
...