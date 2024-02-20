class Restaurant:
    def __init__(self, name,menu=[]):
        self.name = name
        self.revenue = 0
        self.profit = 0
        self.expense = 0
        self.balance = 0
        self.chef = None
        self.menu = menu
        self.manager = None
        self.server = None

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
            self.revenue += amount
            self.balance += amount
            customer.customer_due = 0
            return amount - order.bill

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
