#!/usr/bin/env python3

import sys

def main():
    print('Hello world!\n')

    #integer 
    print('5/3:', (5/3), '\n' '5*3:', (5*3))
    print('5+3:', (5+3), '\n' '5-3:', (5-3))
    print('5**3:', (5**3), '\n' '5//3:', (5//3))
    print()

    #floating point 
    print('5.1/3.2:', (5.1/3.3), '\n' '5.1*3.3:', (5.1*3.3))
    print('5.1+3.2:', (5.1+3.3), '\n' '5.1-3.3:', (5.1-3.3))
    print()

    #reading input from command
    print('what is your name?')
    name = input()
    print('Hi ' + name + '!')

if __name__ == '__main__':
    main()
    sys.exit(0)
 
