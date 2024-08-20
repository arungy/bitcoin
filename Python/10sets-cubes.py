#!/usr/bin/env python3

import sys
import math

def set_encounter():
    n = int( input() )
    m = int( input() )
    
    A = set('')
    print('Enter the Alice set element: ')
    for i in range(n):
        x = int(input())
        A.add(x)
    
    B = set('')
    print('Enter the Bob set element: ')
    for i in range(m):
        x = int(input())
        B.add(x)
        
    comm = A & B
    onlyA = A - comm
    onlyB = B - comm
    
    print('Numerical colors of cubes in both sets: ')
    print(len(comm), ' '.join([str(e) for e in sorted(comm)]))
    
    print('Numerical colors of cubes in Alice: ')
    print(len(onlyA), ' '.join([str(e) for e in sorted(onlyA)]))
    
    print('Numerical colors of cubes in Bob: ')
    print(len(onlyB), ' '.join([str(e) for e in sorted(onlyB)]))
    
    
def main():
    set_encounter()

if __name__ == '__main__':
    main()
    sys.exit(0)
