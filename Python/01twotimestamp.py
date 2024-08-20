#!/usr/bin/env python3

import sys
import math

def main():
    print('Hello world!\n')

    #reading input from command
    h0 = int(input())
    m0 = int(input())
    s0 = int(input())
    
    h1 = int(input())
    m1 = int(input())
    s1 = int(input())

    diff_sec = (h1 * 3600 + m1 * 60 + s1) - (h0 * 3600 + m0 * 60 + s0)

    print('The difference between two time stamps', diff_sec)

if __name__ == '__main__':
    main()
    sys.exit(0)
 
