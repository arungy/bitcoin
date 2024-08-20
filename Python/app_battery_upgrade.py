import sys

from car import Car
from electric_car import ElectricCar

def main():
    ec = ElectricCar('model s', 'Tesla', 2020)
    ec.get_descriptive_name()
    ec.battery.get_range()
    
    ec.battery.upgrade_battery()
    ec.battery.get_range()

if __name__ == '__main__':
    main()
    sys.exit(1)