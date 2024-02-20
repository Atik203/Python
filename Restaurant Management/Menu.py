class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cooking_time = 15


class Burger(Food):
    def __init__(self, name, price, meat, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients
        self.meat = meat


class Pizza(Food):
    def __init__(self, name, price, size, toppings):
        super().__init__(name, price)
        self.size = size
        self.toppings = toppings


class Drink(Food):
    def __init__(self, name, price, is_cold=True):
        super().__init__(name, price)
        self.is_cold = is_cold


# composition (HAS-A relationship)
class Menu:
    def __init__(self):
        self.pizzas = []
        self.burgers = []
        self.drinks = []

    def add_food_item(self, food_item, food_type):
        if food_type == "pizza":
            self.pizzas.append(food_item)
        elif food_type == "burger":
            self.burgers.append(food_item)
        elif food_type == "drink":
            self.drinks.append(food_item)
        else:
            print("Invalid food type")

    def remove_food_item(self, food_item, food_type):
        if food_type == "pizza":
            self.pizzas.remove(food_item)
        elif food_type == "burger":
            self.burgers.remove(food_item)
        elif food_type == "drink":
            self.drinks.remove(food_item)
        else:
            print("Invalid food type")

    def show_menu(self):
        print("Pizzas:")
        for pizza in self.pizzas:
            print(f"{pizza.name} - {pizza.price}")

        print("Burgers:")
        for burger in self.burgers:
            print(f"{burger.name} - {burger.price}")

        print("Drinks:")
        for drink in self.drinks:
            print(f"{drink.name} - {drink.price} - is cold - {drink.is_cold}")
