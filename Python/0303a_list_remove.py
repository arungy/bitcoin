#!/usr/bin/python

import sys

def main():
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    
    #modify the elements in the list
    motorcycles[0] = 'ducati'
    print(motorcycles)
    
    #add new element to the list
    motorcycles = []
    motorcycles.append('ducati')
    motorcycles.append('bajaj')
    motorcycles.append('honda')
    motorcycles.append('ktm')
    
    motorcycles.insert(2, 'suzuki')
    print(motorcycles)
    
    #remove the element based on position
    del motorcycles[0]
    print(motorcycles)
    
    print()
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    
    #last_owned = motorcycles.pop()
    #print("The last motorcycle I owned was a " + last_owned.title() + ".")
    
    first_owned = motorcycles.pop(0)
    print("The first motorcycle I owned was " + first_owned.title() + ".")
    print(motorcycles)
    
    #removing the element by value
    print()
    motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
    print(motorcycles)
    
    expensive_bike = 'ducati'
    motorcycles.remove(expensive_bike)
    print(motorcycles)
    
    print("\nA " + expensive_bike.title() + " is too expensive for me.")
    
if __name__ == '__main__':
    main()
    sys.exit(0)
