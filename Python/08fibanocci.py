#!/usr/bin/env python3

import sys
import math

#1,1,2,3,5,8,13,21,
def fibanocci(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibanocci(n-1) + fibanocci(n-2)

def main():
    print('enter the \'n\' value')
    n = int(input())
    print('fibanocci(%d): %d' % (n, fibanocci(n)))

if __name__ == '__main__':
    main()
    sys.exit(0)