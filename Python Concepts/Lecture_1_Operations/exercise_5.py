# ================================
# Exercise: Comparison & Boolean Operations
# ================================

# Given values
age = 20
minimum_age = 18
has_license = True
is_insured = False

# Task 1: Check if person is an adult (age greater equal to minimum_age)
is_adult = age >= minimum_age

# Task 2: Check if person can drive (is adult and has license)
can_drive = is_adult and has_license

# Task 3: Check if person can legally drive a car (can drive and is insured)
can_legally_drive = can_drive and is_insured

# Task 4: Check if person needs parental consent (is not an adult)
needs_consent = not is_adult

# Task 5: Check if person qualifies for student discount (age between 18 and 25 inclusive)
student_discount = age >= 18 and age <=25

print(f"Is adult: {is_adult}")
print(f"Can drive: {can_drive}")
print(f"Can legally drive: {can_legally_drive}")
print(f"Needs parental consent: {needs_consent}")
print(f"Qualifies for student discount: {student_discount}")
