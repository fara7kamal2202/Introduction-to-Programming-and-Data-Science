# ================================
# Exercise: Working with Classes
# ================================

# Task 1: Copy the code from the slides and print the age of bob (using the dot notation)
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)


# ================================
# Task 2: Create an if-statement that prints the name of the oldest of the two Persons
# ================================

print(alice.name if alice.age > bob.age else bob.name)


# ================================
# Task 3: Create three other Persons. Make a list called people with all 5 Persons.
# ================================

jason = Person("Jason", 32)
jeremiah = Person("Jeremiah", 24)
jasinda = Person("Jasinda", 55)
people = [alice, bob, jason, jeremiah, jasinda]
# ================================
# Task 4: Make a loop that finds and prints the youngest person’s name
# ================================
min_age = people[0].age
for person in people:
    if person.age < min_age:
        min_age = person.age
print(min_age)



