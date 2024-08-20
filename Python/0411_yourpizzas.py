#!/usr/bin/python

import sys

def main():
    my_pizzas = ['pizza', 'falafel', 'carrot cake']
    friend_pizzas = my_pizzas[:]
    
    my_pizzas.append('Jelly')
    friend_pizzas.append('Spice Cheese')
    
    print("My favorite pizzas are:")
    for pizza in my_pizzas:
        print(pizza.title())
        
    print("\nFriend's favorite pizzas are:")
    for pizza in friend_pizzas:
        print(pizza.title())

if __name__ == '__main__':
    main()
    sys.exit(0)