#!/usr/bin/env python3

import sys
import math
from math import ceil

def main():
    print('Hello world!\n')

    x = int(input())
    d1 = x // 100
    d2 = (x % 100) // 10
    d3 = (x % 10)

    print('sum digit is', d1 + d2 + d3)
    

if __name__ == '__main__':
    main()
    sys.exit(0)
 
