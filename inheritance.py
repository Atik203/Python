"""
Inheritance is a way of creating a new class for using details of an existing class without modifying it.
The newly formed class is a derived class (or child class).
Similarly, the existing class is a base class (or parent class).

base class or parent class, common attributes and functionality
derived class or child class, uncommon attributes and functionality

"""


class BaseClass:
    pass


class DerivedClass(BaseClass):
    pass


"""
1.Simple inheritance: parent class --> child class (Device --> Laptop)
2.Multilevel inheritance: parent class --> child class --> grandchild class (Device --> Laptop --> Phone)
3.Multiple inheritance: child class --> parent class1, parent class2 (Laptop --> Device, Camera)
4.Hybrid inheritance: combination of two or more types of inheritance (Device --> Laptop, Phone, Camera)

"""


class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def run(self):
        return f'{self.brand} {self.model} Device is running'


class Laptop:
    def __init__(self,brand,model,price, memory):
        self.memory = memory
        super().__init__(brand, model, price)

    def coding(self):
        return f'Learning is coding'


class Phone:
    def __init__(self,brand,model,price ,color):
        self.color = color
        super().__init__(brand, model, price)

    def call(self):
        return f'Calling to someone'


class Camera:
    def __init__(self,brand,model,price, pixel):
        self.pixel = pixel
        super().__init__(brand, model, price)

    def capture(self):
        return f'Capturing the moment'
