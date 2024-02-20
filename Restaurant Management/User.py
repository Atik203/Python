from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, phone, email, adress):
        self.name = name
        self.phone = phone
        self.email = email
        self.adress = adress


class Customer(User):
    def __init__(self, name, phone, email, adress):
        super().__init__(name, phone, email, adress)
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

    def eat_food(self, order):
        print(f"{self.name} is eating {order.items}")

    def pay_for_order(self, amount):
        # TODO: submit the money to manager
        pass

    def give_tips(self, amount):
        pass

    def write_review(self, stars):
        pass


class Employee(User):
    def __init__(self, name, phone, email, address, salary, start_date, department):
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.start_date = start_date
        self.department = department
        self.due = salary

    def receive_salary(self):
        self.due = 0


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, start_date, department, cooking_item):
        super().__init__(name, phone, email, address, salary, start_date, department)
        cooking_item = cooking_item


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, start_date, department):
        super().__init__(name, phone, email, address, salary, start_date, department)
        self.tips_earning = 0

    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self, order):
        print(f"{self.name} served order {order.items}")

    def receive_tips(self, amount):
        self.tips_earning += amount


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, start_date, department):
        super().__init__(name, phone, email, address, salary, start_date, department)

    def manage_employee(self, employee):
        pass

    def manage_order(self, order):
        pass