#!/usr/bin/env python3

import sys
import math

def set_equalnum():
    print('Enter the set element for A: ')
    A = set(input().split())
    
    print('Enter the set element for B: ')
    B = set(input().split())
    
    print('equal elements: %d' % (len(A & B)))

def main():
    set_equalnum()

if __name__ == '__main__':
    main()
    sys.exit(0)
