#!/usr/bin/env python3

import sys
import math

def set_distinct_word():
    print('Enter the number of lines: ')
    n = int( input() )
    
    A = set('')
    print('Enter the %d lines below: ' % (n))
    for i in range(n):
        B = set(input().split())
        A |= B
    
    print('number of distinct words: %d' % (len(A)))

def main():
    set_distinct_word()

if __name__ == '__main__':
    main()
    sys.exit(0)
