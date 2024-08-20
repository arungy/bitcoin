"""A class that can be used to represent a car."""

class Car:
    """ Attempt to model a car """

    def __init__(self, model, brand, make):
        self.model = model
        self.brand = brand
        self.make = make
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(f"\n{self.brand} released {self.model} by {self.make}")

    def update_odometer(self, odometer):
        if odometer > self.odometer_reading:
            self.odometer_reading = odometer
        else:
            print(f"Odometer read can't roll back")

    def read_odometer(self):
        print(f"Odometer reading: {self.odometer_reading}")

    def increment_odometer(self, new_reading):
        self.odometer_reading += new_reading
