class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __repr__(self):
        return f'{self.brand} {self.model} {self.price}'


class Bus(Vehicle):
    def __init__(self, brand, model, price, seat):
        self.seat = seat
        super().__init__(brand, model, price)


class Truck(Vehicle):
    def __init__(self, brand, model, price, capacity):
        self.capacity = capacity
        super().__init__(brand, model, price)


class Pickup(Truck):
    def __init__(self, brand, model, price, capacity):
        super().__init__(brand, model, price, capacity)


class AcBus(Bus):
    def __init__(self, brand, model, price, seat, temperature):
        self.temperature = temperature
        super().__init__(brand, model, price, seat)

    def __repr__(self) -> str:
        return super().__repr__() + f' {self.temperature}'



acbus = AcBus('Tata', 'AC', 1000000, 50, 20)
print(acbus)