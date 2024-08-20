#!/usr/bin/python

import sys

def main():
    cars = ['audi', 'bmw', 'toyota', 'tesla']

    for car in cars:
        if car == "bmw":
            print(car.upper())
        else:
            print(car.title())
     
    print()
    #case sensitive comparision
    car = 'Audi'
    print(car == 'audi')
    print(car.lower() == 'audi')

if __name__ == '__main__':
    main()
    sys.exit(0)