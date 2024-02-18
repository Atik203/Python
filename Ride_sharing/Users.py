from abc import ABC, abstractmethod
from datetime import datetime


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
    def __init__(self, name, email, nid, current_location):
        self.current_ride = None
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, nid)
        self.__id = "R" + str(self.__nid)

    def display_profile(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nNID: {self.__nid}\nID: {self.__id}\nWallet: {self.wallet}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, location, destination):
        if not self.current_ride:
            ride_request = Ride_request(self, destination)
            ride_matching = Ride_matching()
            self.current_ride = ride_matching.find_driver(ride_request)


class Driver(User):
    def __init__(self, name, email, nid, current_location):
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, nid)
        self.__id = "D" + str(self.__nid)

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


class Ride_request:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location


class Ride_matching:
    def __init__(self):
        self.available_drivers = []

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            # TODO: find the closest driver
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride
