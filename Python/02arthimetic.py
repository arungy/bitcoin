#!/usr/bin/env python3

import sys
import math
from math import ceil

def main():
    print('Hello world!\n')

    print(17 / 3)
    print(2 ** 3)
    print(2 ** -2)
    print()

    print(17 / 3)
    print(17 // 3)
    print(17 % 3)
    print()

    x = float(input())
    print(x)

    print(int(1.3))
    print(int(1.7))
    print(int(-1.3))
    print(int(-1.7))
    print()
    
    print(round(1.3))
    print(round(1.7))
    print(round(-1.3))
    print(round(-1.7))
    print()

    print(0.1 + 0.2)
    print()

    x = math.ceil(4.2)
    print(x)
    print(math.ceil(1 + 3.8))

    x = 7/ 2
    y = ceil(x)
    print(y)
    

if __name__ == '__main__':
    main()
    sys.exit(0)
 
