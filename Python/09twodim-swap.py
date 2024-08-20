#!/usr/bin/env python3

import sys
import math

def twodim_swap():
    print('Enter the number of elemnts: ')
    rowN = int( input() )
    colM = int( input() )
    
    entry = [[-1 for x in range(colM)] for y in range(rowN)]
    entry = [[x for x in input().split()] for y in range(rowN)]
    
    print('Enter the swap columns: ')
    i = int( input() )
    j = int( input() )
    
    for y in range(len(entry)):
        for x in range(len(entry[y])):
            if x == j:
                t = entry[y][j]
                entry[y][j] = entry[y][i]
                entry[y][i] = t
                
    for ele in entry:
        print(' '.join([str(x) for x in ele]))

def main():
    twodim_swap()

if __name__ == '__main__':
    main()
    sys.exit(0)
