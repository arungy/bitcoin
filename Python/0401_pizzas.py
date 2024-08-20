#!/usr/bin/python

import sys

def main():
    pizzas = ['margretta', 'classic cheese', 'double cheese']
    
    for pizza in pizzas:
        print("I like " + pizza.title() + " pizza.")
    
    print("\nI really love all these delicious pizzas!")
    
if __name__ == '__main__':
    main()
    sys.exit(0)
