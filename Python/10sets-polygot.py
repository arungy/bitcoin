#!/usr/bin/env python3

import sys
import math

def set_polygot():
    print('Enter the number of element: ')
    n = int( input() )
    
    entry = [[''] * n for y in range(n)]
    
    print('Enter the elements: ')
    for x in range(0, n):
        entry[x] = input().split()
    
    ALL = ONE = set(entry[0])
    for x in range(1, n):
        ONE = ONE & set(entry[x])
        ALL = ALL | set(entry[x])
    
    print(len(ONE))
    print(' '.join([x for x in sorted(ONE)]))
    
    print(len(ALL))
    print(' '.join([x for x in sorted(ALL)]))

def main():
    set_polygot()

if __name__ == '__main__':
    main()
    sys.exit(0)
