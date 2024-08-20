#!/usr/bin/python

import sys

def main():
    animals = ['cat', 'dog', 'horse']
    
    for animal in animals:
        print("A " + animal.title() + " would make a great pet.")
    
    print("\nAny of these animals would make a great pet!")
    
if __name__ == '__main__':
    main()
    sys.exit(0)
