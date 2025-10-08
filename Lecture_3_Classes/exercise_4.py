# ================================
# Exercise: Restaurant Menu System
# ================================

# Task 1: Create a new class called Food, it should have name, price and description as attributes.

class Food:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

# ================================
# Task 2: Instantiate at least three different foods you know and like.
# ================================

pizza = Food("Pizza", 18, "pizza from napoli")
burger = Food("Burger", 17, "burger from the us")
noodles = Food("Noodles", 15, "Noodlessss")


# ================================
# Task 3: Create a new class called Menu, it should have a list (of Foods) as attribute.
# __init__ should take a list of Foods as optional parameters (default=[])
# ================================

class Menu:
    def __init__(self, foods = None):
        self.foods = foods

    def add_food(self, food):
        if self.foods == None:
            self.foods = [food]
        else:
            self.foods.append(food)

    def remove_food(self, food):
        if food in self.foods:
            self.foods.remove(food)

    def print_prices(self):
        for food in self.foods:
            print(f"{food.name}: {food.price}€")

    def get_average_price(self):
        total = 0
        for food in self.foods:
            total += food.price
        return total / len(self.foods)


# ================================
# Task 4: Create a addFood() and removeFood() for the Menu
# ================================

...


# ================================
# Task 5: Create a few new Food instances. Add each to the Menu using the respective Method.
# ================================

...


# ================================
# Task 6: Add a method printPrices() that list all items on the Menu with their prices.
# ================================

...


# ================================
# Task 7: Add a Menu method getAveragePrice() that returns the average Food price of the Menu
# ================================

...
