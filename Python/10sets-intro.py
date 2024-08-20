#!/usr/bin/env python3

import sys
import math

def sets():
    A = {1, 2, 3}
    A = set('qwerty')
    print(A)
    
    A1 = {1, 2, 3}
    A2 = {3, 2, 3, 1}
    print(A1 == A2)
    print( 1 in A1, 4 not in A1)
    
    if (4 not in A1):
        A1.add(4)
        
    print(' '.join([str(num) for num in A1]))
    
    if 4 in A1:
        A1.remove(4)
    
    print(' '.join([str(num) for num in A1]))

def main():
    sets()

if __name__ == '__main__':
    main()
    sys.exit(0)
