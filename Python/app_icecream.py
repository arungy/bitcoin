"""A class that can be used as ice cream"""

import sys
from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cusine_type, flavors):
        super().__init__(restaurant_name, cusine_type)
        self.flavors = flavors

    def read_icecream_flavors(self):
        print(f"{self.restaurant_name} icecream flavours: {self.flavors.title()}")

def main():
    ics = IceCreamStand('BBQ Nation', 'multicusine', 'strawberry')

    ics.read_icecream_flavors()

if __name__ == '__main__':
    main()
    sys.exit(1)
