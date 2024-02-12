"""
Encapsulation is the process of restricting access to certain parts of an object. In OOP, encapsulation is used to
refer to one of two related but distinct notions, and sometimes to the combination thereof: A language mechanism for
restricting direct access to some of the object components.

"""


class Bank:
    def __init__(self, name, balance):
        self._name = name  # protected attribute
        self.__balance = balance  # private attribute

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def __str__(self):
        return f'Name: {self._name}, Balance: {self.__balance}'


john = Bank('John', 1000)
print(john)
print(john._Bank__balance)  # accessing private attribute
