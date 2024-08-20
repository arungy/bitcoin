#!/usr/bin/env python3

import sys
import math

def main():
    print('Hello world!\n')

    #reading input from command
    b = int(input())
    h = int(input())

    print('area of right-angle triangle:', math.sqrt((b*b) + (h*h)))

if __name__ == '__main__':
    main()
    sys.exit(0)
 
