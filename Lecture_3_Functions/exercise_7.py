# ================================
# Exercise: Write a function check_each(), which takes a list of numbers as argument.
# Using a for loop, iterate through the list.
# For each number, print "bigger" if it's bigger than 5, "smaller" if it's smaller than 5,
# and "equal" if it's equal to 5.
# Test your function with different lists.
# ================================

# Write your function here:
def check_each(numbers_list):
    number_to_check = 5
    for value in numbers_list:
        if value == number_to_check:
            verdict = "equal"
        elif value > number_to_check:
            verdict = "bigger"
        else:
            verdict = "smaller"
        print(verdict)

# Test your function with these lists (change them to test more):
test_list1 = [1, 5, 10, 3, 7]  # Mix of values
check_each(test_list1)

print("---")  # Separator for clarity

test_list2 = [5, 5, 5]  # All equal to 5
check_each(test_list2)

print("---")  # Separator for clarity

test_list3 = [2, 4, 6, 8]  # Different values
check_each(test_list3)
