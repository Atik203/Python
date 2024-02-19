from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name):
        self.name = name


class Customer(User):
    def __init__(self, name):
        super().__init__(name)
        self.__order = None

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        print(f"{self.name} placed order {order.items}")

    def eat_food(self,order):
        print(f"{self.name} is eating {order.items}")

    def pay_for_order(self, amount):
        # TODO: submit the money to manager
        pass

    def give_tips(self, amount):
        pass

    def write_review(self, stars):
        pass
