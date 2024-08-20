#!/usr/bin/env python3

import sys
import math

def power(a, n):
    res = 1
    if n < 0:
        s = n
        e = 0
    else:
        s = 1
        e = n + 1
    
    for i in range(s, e):
        if n > 0:
            res *= a
        elif n < 0:
            res /= a
        else:
            res = 1
        
    return res

def main():
    print('enter the a value:')
    a = float(input())
    
    print('enter the n value:')
    n = int(input())
    
    print('power(%f, %f): %f' % (a, n, power(a, n)))


if __name__ == '__main__':
    main()
    sys.exit(0)