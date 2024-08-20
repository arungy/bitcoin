#!/usr/bin/env python3

import sys
import math

def twodim_max():
    entry = []
    
    print('Enter the number of rows: ')
    col = int( input() )
    
    for n in range(col):
        entry.append([int(x) for x in input().split()])
    
    max = 0
    mx = 0
    my = 0
    for y in range(len(entry)):
        for x in range(len(entry[y])):
            if entry[y][x] < max:
                max = entry[y][x]
                mx = x
                my = y
    
    print('my: %d, mx: %d' % (my, mx))

def main():
    twodim_max()

if __name__ == '__main__':
    main()
    sys.exit(0)
