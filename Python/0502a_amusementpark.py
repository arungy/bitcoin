#!/usr/bin/python

import sys

def main():
    age = 12
    
    if age < 4:
        price = 0
    elif age < 18:
        price = 5
    else:
        price = 10

    print("Your admission cost is $" + str(price) + ".")
    
if __name__ == '__main__':
    main()
    sys.exit(0)