#!/usr/bin/env python3

import sys
import math

def set_encounter():
    print('Enter the set element: ')
    A = input().split()
    
    entry = set('')
    for x in A:
        if x in entry:
            print('YES')
        else:
            print('NO')
        entry.add(x)
    
def main():
    set_encounter()

if __name__ == '__main__':
    main()
    sys.exit(0)
