from math import pi

"""
-polymorphism is the ability to use a common interface for multiple forms (data types).
-It is a way to provide a single interface to different data types.
-It is a way to perform a single action in different ways.

"""


class Shape:
    def __init__(self, name):
        self.name = name


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle("Circle", 4)
print(c.area())

r = Rectangle("Rectangle", 4, 5)
print(r.area())

t = Triangle("Triangle", 4, 5)
print(t.area())
