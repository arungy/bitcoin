#!/usr/bin/env python3

import sys
import math

def twodim_max():
    print('Enter the number of rows: ')
    n = int( input() )
    
    entry = [['.' for x in range(n)] for y in range(n)]
    
    nby2 = int(n/2)
    for y in range(len(entry)):
        for x in range(len(entry[y])):
            if x == nby2 or y == nby2 or x == y or (x + y + 1) == n:
                entry[y][x] = '*'
                
    for ele in entry:
        print(' '.join([x for x in ele]))

def main():
    twodim_max()

if __name__ == '__main__':
    main()
    sys.exit(0)
