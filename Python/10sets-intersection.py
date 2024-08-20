#!/usr/bin/env python3

import sys
import math

def set_intersection():
    print('Enter the set element for A: ')
    A = set(input().split())
    
    print('Enter the set element for B: ')
    B = set(input().split())
    
    print('intersection sets:', ' '.join([str(e) for e in sorted(A & B)]))

def main():
    set_intersection()

if __name__ == '__main__':
    main()
    sys.exit(0)
