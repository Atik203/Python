from abc import ABC, abstractmethod
from datetime import datetime


class Ride_sharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.rides = []
        self.riders = []
        self.drivers = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self):
        return f"{self.company_name} has {len(self.riders)} riders and {len(self.drivers)} drivers."


class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.__nid = nid
        # TODO: have to add the id dynamically
        self.__id = 0
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


def request_ride(location, destination):
    print(f"Requesting a ride from {location} to {destination}.")


class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        self.current_ride = None
        self.current_location = current_location
        self.wallet = initial_amount
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nNID: {self.__nid}\nID: {self.__id}\nWallet: {self.wallet}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self,ride_sharing, destination):
        if not self.current_ride:
            ride_request = Ride_request(self, destination)
            ride_matching = Ride_matching(ride_sharing.drivers)
            self.current_ride = ride_matching.find_driver(ride_request)

    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nNID: {self.__nid}\nID: {self.__id}\nWallet: {self.wallet}")

    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.estimated_fare = None
        self.start_time = None
        self.end_time = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= amount
        self.driver.wallet += amount

    def __repr__(self):
        return f"Ride from {self.start_location} to {self.end_location}."


class Ride_request:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class Ride_matching:
    def __init__(self,drivers):
        self.available_drivers = drivers

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            # TODO: find the closest driver
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride


class Vehicle:
    speed = {
        "bike": 40,
        "car": 60,
        "bus": 30
    }

    def __init__(self, vehicle_type, plate_number, rate):
        self.vehicle_type = vehicle_type
        self.plate_number = plate_number
        self.rate = rate
        self.status = "available"

    @abstractmethod
    def start_drive(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, plate_number, rate):
        super().__init__(vehicle_type, plate_number, rate)

    def start_drive(self):
        self.status = "unavailable"


# check the class integration

pathao = Ride_sharing("Pathao")
rider1 = Rider("Rahim", "rahim@gmail.com", 123456, "Dhanmondi", 1000)
rider2 = Rider("Karim", "karim@gmail.com", 123457, "Mirpur", 500)
pathao.add_rider(rider1)
pathao.add_rider(rider2)
driver1 = Driver("Kamal", "kamal@gmail.com", 123458, "Mohakhali")
driver2 = Driver("Jamal", "jamal@gmail.com", 123459, "Banani")
pathao.add_driver(driver1)
pathao.add_driver(driver2)
rider1.request_ride(pathao,"Banani")
rider1.show_current_ride()
