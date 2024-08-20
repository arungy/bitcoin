#!/usr/bin/env python3

import sys
import math

def twodim_matrix():
    print('Enter the number of elemnts: ')
    rowN = int( input() )
    colM = int( input() )
    
    entry = [[-1 for x in range(colM)] for y in range(rowN)]
    matrix = [[-1 for x in range(colM)] for y in range(rowN)]
    
    entry = [[x for x in input().split()] for y in range(rowN)]
    
    print('Enter the C element: ')
    c = int( input() )
    
    for y in range(len(entry)):
        for x in range(len(entry[y])):
            matrix[y][x] = int(entry[y][x]) * c
                
    for ele in matrix:
        print(' '.join([str(x) for x in ele]))

def main():
    twodim_matrix()

if __name__ == '__main__':
    main()
    sys.exit(0)
