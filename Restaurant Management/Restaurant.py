class Restaurant:
    def __init__(self, name, rent, menu=[]):
        self.name = name
        self.revenue = 0
        self.profit = 0
        self.expense = 0
        self.balance = 0
        self.rent = rent
        self.chef = None
        self.menu = menu
        self.manager = None
        self.server = None
        self.orders = []

    def add_employee(self, employee_type, employee):
        if employee_type == "chef":
            self.chef = employee
        elif employee_type == "manager":
            self.manager = employee
        elif employee_type == "server":
            self.server = employee
        else:
            print("Invalid employee type")

    def received_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill

        else:
            print("Insufficient payment")

    def pay_expense(self, amount, description):
        if amount <= self.balance:
            self.balance -= amount
            self.expense += amount
            print(f"Paid {amount} for {description}")

        else:
            print("Insufficient balance")

    def pay_salary(self, employee):
        if employee.salary <= self.balance:
            self.balance -= employee.salary
            employee.receive_salary()
        else:
            print("Insufficient balance")

    def show_employee(self):
        if self.chef:
            print(f"Chef: {self.chef.name}")
        if self.manager:
            print(f"Manager: {self.manager.name}")
        if self.server:
            print(f"Server: {self.server.name}")

    def add_order(self, order):
        self.orders.append(order)
        print(f"Order added to {self.name}")
