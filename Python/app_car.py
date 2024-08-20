import sys

from car import Car
from electric_car import ElectricCar

def main():
    cr = Car('Jippsy', 'Maruti', 1997)
    cr.get_descriptive_name()

    cr.update_odometer(65)
    cr.read_odometer()

    cr.increment_odometer(50)
    cr.read_odometer()

    ec = ElectricCar('model s', 'Tesla', 2020)
    ec.get_descriptive_name()
    ec.battery.describe_battery()
    ec.battery.get_range()

if __name__ == '__main__':
    main()
    sys.exit(1)