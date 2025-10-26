
# ================================
# Exercise: Animal Class
# ================================

class Animal:

    def __init__(self, name, legs, canSwim, canFly):
        self.name = name
        self.legs = legs
        self.canSwim = canSwim
        self.canFly = canFly

    def set_legs(self, legs):
        self.legs = legs

    def get_legs(self):
        return self.legs

    def print_info(self):
        print("Name: " + self.name)
        print("Legs: " + str(self.legs))
        print("CanSwim: " + str(self.canSwim))
        print("CanFly: " + str(self.canFly))


# ================================
# Task 1: Create two realistic instances of Animal
# ================================

cat = Animal("Cat_1", 4, False, False)
dog = Animal("Dog_1", 4, False, False)


# ================================
# Task 2: Print the name of each object
# ================================

print(cat.get_legs())
print(dog.get_legs())


# ================================
# Task 3: Change the amount of legs of one object using the dot notation
# ================================

cat.legs = 3


# ================================
# Task 4: Add a method setLegs() to set the amount of legs of an object and repeat task 3 but this time using this new method.
# ================================

cat.set_legs(3)


# ================================
# Task 5: Add a method getLegs() to return the amount of legs
# ================================

cat.get_legs()

# ================================
# Task 6: Add a method named printInfo that prints all attributes of the Animal
# ================================

cat.print_info()
dog.print_info()


