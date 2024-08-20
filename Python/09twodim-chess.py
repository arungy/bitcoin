#!/usr/bin/env python3

import sys
import math

def twodim_chess():
    print('Enter the number of rows: ')
    j = int( input() )
    i = int( input() )
    
    entry = [['.' for x in range(i)] for y in range(j)]
    
    for y in range(len(entry)):
        for x in range(len(entry[y])):
            if ((x % 2) == 1 and (y % 2) == 0) or ((x % 2) == 0 and (y % 2) == 1) :
                entry[y][x] = '*'
                
    for ele in entry:
        print(' '.join([x for x in ele]))

def main():
    twodim_chess()

if __name__ == '__main__':
    main()
    sys.exit(0)
