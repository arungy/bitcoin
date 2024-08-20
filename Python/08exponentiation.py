#!/usr/bin/env python3

import sys
import math

def exponentiation(a, n):
    
    if n == 0:
        return 1
    else:
        return a * exponentiation(a, n-1)

def main():
    print('enter the \'a\' value:')
    a = float(input())
   
    print('enter the \'n\' value:')
    n = int(input())
    
    print('exponentiation(%f, %d): %f' % (a, n, exponentiation(a, n)))

if __name__ == '__main__':
    main()
    sys.exit(0)