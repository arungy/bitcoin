#!/usr/bin/python

import sys

def main():
    dimensions = (200, 50)

    #dimensions[0] = 250     #assign value to element in tuple gives 'error'
    
    print("Original dimensions: ")
    for dimension in dimensions:
        print(dimension)
    
    dimensions = (400, 100)
    print("\nModified dimensions: ")
    for dimension in dimensions:
        print(dimension)

if __name__ == '__main__':
    main()
    sys.exit(0)