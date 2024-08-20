"""A class that can be used to represent a battery for an electric car."""

from car import Car

class Battery():
    """ An attempt to model a battery for an electric car """

    def __init__(self, battery=75):
        self.battery_size = battery

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
        print(f"Battery capacity is upgraded in this car.")


class ElectricCar(Car):
    """ Attempt to model an electric car """
    def __init__(self, model, brand, make):
        super().__init__(model, brand, make)

        self.battery = Battery()
