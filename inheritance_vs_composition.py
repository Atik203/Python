# inheritance vs composition

"""
inheitance:
    - "is a" relationship
    - is a mechanism for code reuse
    - is a mechanism for code organization
    - is a mechanism for polymorphism

composition:
    - "has a" relationship
    - is a mechanism for code reuse
    - is a mechanism for code organization
    - is a mechanism for polymorphism

"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Furniture:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class House: # house has a furniture
    def __init__(self, name):
        self.name = name
        self.furniture = Furniture("Sofa")
