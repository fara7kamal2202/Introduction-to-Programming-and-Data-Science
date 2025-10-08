# =================================================
# Exercise: Working with Lists
# =================================================

# Create a list named numbers containing integers from 1 to 5
# numbers = [1, 2, 3, 4, 5]
numbers = [i for i in range(1, 6)]
print(f"Original Numbers List: {numbers}")
...

# Append the number 6 to the end of the list
numbers.append(6)
print(f"Numbers List, Added 6: {numbers}")
...

# Remove the number 3 from the list
numbers.remove(3)
print(f"Numbers List, Removed 3: {numbers}")
...

# Insert the number 0 at the beginning of the list
# Search on the internet how to solve this task.
# Hint: the function is called .insert()
numbers.insert(0, 0)
print(f"Numbers List, Added 0 at Beginning: {numbers}")
...

# Print the modified list
print(f"Modified Numbers List: {numbers}")
...

# Use the list from Task 1. Save the first element of the list in a variable first_item. Print it.
first_element = numbers[0]
print(f"First Element: {first_element}")
...

# Save the last item in a variable last_item. Print it.
last_item = numbers[-1]
print(f"Last Element: {last_item}")
...

# Save the 3rd element in a variable third_item. Print it.
third_item = numbers[2]
print(f"Third Element: {third_item}")
...

# Save the second-to-last element in a variable second_to_last. Print it.
second_to_last = numbers[-2]
print(f"Second To Last: {second_to_last}")
...

# Save the first 3 elements in a variable first_three. Print it.
first_three = numbers[:3]
print(f"First Three Elements: {first_three}")
...

# Print the first element of first_three.
first_element = first_three[0]
print(f"First of Three Elements: {first_element}")
...

# Save the 2nd and 3rd element of the list numbers in a variable second_third. Print it.
second_third = numbers [1:3]
print(f"Second and Third Elements: {second_third}")
...
