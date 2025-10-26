# ================================
# Exercise: Grade Classifier
# ================================

# Instructions:
# Write a Python program that takes a numeric grade as input and prints out the corresponding letter grade according to the following criteria:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

grade = int(input("Enter your numeric grade: "))

if grade > 100 or grade < 0:
    print("Invalid grade")
else:
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"