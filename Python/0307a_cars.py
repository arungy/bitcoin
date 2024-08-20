#!/usr/bin/python

import sys

def main():
    #sort() function
    cars = ['audi', 'bmw', 'toyota', 'subaru']
    print("Orginal list: ", cars)
    
    cars.sort()
    print("Sort list: ", cars)
    
    cars.sort(reverse=True)
    print("Reverse Sort list: ", cars)
    
    print()
    #sorted function
    cars = ['audi', 'bmw', 'toyota', 'subaru']
    print('Here is the original list:', cars)
    
    print('Here is the sorted list:', sorted(cars))
    
    print('Here is the original list again:', cars)
    
    #reverse() function
    cars.reverse()
    print(cars)
    
    cars.reverse()
    print(cars)
    
    #length of list
    print(len(cars))
    
    
if __name__ == '__main__':
    main()
    sys.exit(0)
