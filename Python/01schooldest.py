#!/usr/bin/env python3

import sys
import math

def main():
    print('Hello world!\n')

    #reading input from command
    fc = int(input())
    sc = int(input())
    tc = int(input())

    total_desk = (int(fc/2) + (fc%2)) + (int(sc/2)+(sc%2)) + (int(tc/2)+(tc%2))

    print('Minimum of total desks required', total_desk)

if __name__ == '__main__':
    main()
    sys.exit(0)
 
