#!/usr/bin/env python3

import sys
import math

def twodim_diagonal():
    print('Enter the number of elemnts : ')
    n = int( input() )
    
    entry = [[0 for x in range(n)] for y in range(n)]
    
    for y in range(len(entry)):
        for x in range(len(entry[y])):
            entry[y][x] = abs(y - x)
                
    for ele in entry:
        print(' '.join([str(x) for x in ele]))

def main():
    twodim_diagonal()

if __name__ == '__main__':
    main()
    sys.exit(0)
