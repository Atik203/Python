from abc import ABC,abstractmethod

"""

********** Abstract Base Class **********
- Abstract Base Class (ABC) is a module in Python that provides the infrastructure for defining Abstract Base Classes.
- Abstract Base Classes are classes that contain one or more abstract methods.
- Abstract Base Classes cannot be instantiated and can only be used for inheritance.

********** Abstract Method **********
- Abstract Method is a method that is declared, but contains no implementation.
- Abstract Method can only be defined in Abstract Base Class.
- Abstract Method can only be implemented in the derived class.


********** Abstract vs Interface **********
- Abstract Base Class is a class that contains one or more abstract methods.
- Interface is a class that contains only abstract methods.
- In Python, there is no interface. We can use Abstract Base Class to define an interface.
- In Python, we can provide implementation in Abstract Base Class, but in Interface, we cannot provide implementation.


********** How to create Abstract Base Class **********
- To create an Abstract Base Class, we need to import ABC and abstractmethod from the abc module.
- We need to inherit the ABC class and use the @abstractmethod decorator to define an abstract method.

"""



class Animal(ABC):
    @abstractmethod
    def __init__(self):
        print("Animal created")
    @abstractmethod
    def speak(self):   # enforce the derived class to implement this method
        print("Animal speaking")

class Dog(Animal):
    def __init__(self):
        print("Dog created")
        super().__init__()
    def speak(self):
        print("Dog speaking")


d = Dog()
d.speak()



