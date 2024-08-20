#!/usr/bin/python

import sys

def main():
    requested_topping = 'mushrooms'
    
    if requested_topping != 'anchovies':
        print("Hold the anchovies!")

if __name__ == '__main__':
    main()
    sys.exit(0)