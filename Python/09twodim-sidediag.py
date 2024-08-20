#!/usr/bin/env python3

import sys
import math

def twodim_sidediag():
    print('Enter the number of elemnts : ')
    n = int( input() )
    
    entry = [[-1 for x in range(n)] for y in range(n)]
    
    for y in range(len(entry)):
        for x in range(len(entry[y])):
            s = y + x + 1
            if s == n:
                entry[y][x] = 1
            elif s < n:
                entry[y][x] = 0
            else :
                entry[y][x] = 2
                
    for ele in entry:
        print(' '.join([str(x) for x in ele]))

def main():
    twodim_sidediag()

if __name__ == '__main__':
    main()
    sys.exit(0)
