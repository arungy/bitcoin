#!/usr/bin/env python3

import sys
import math

def sets():
    A = set(input().split())
    
    print('distinct elements: %d' % (len(A)))

def main():
    sets()

if __name__ == '__main__':
    main()
    sys.exit(0)
