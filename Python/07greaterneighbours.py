#!/usr/bin/python

import sys

def main():
    print('enter the no. of elements:')
    elements = [int(input()) for e in range(int(input()))]
    n = 0    
    
    print('\nOutput')
    prev = elements[0]
    cur  = elements[1]
    for next in elements[2:]:
        if cur > prev and cur > next :
            n += 1
        prev = cur
        cur = next
    print(n)

if __name__ == '__main__':
    main()
    sys.exit(0)
        