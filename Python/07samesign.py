#!/usr/bin/python

import sys

def main():
    print('enter the no. of elements:')
    elements = [int(input()) for e in range(int(input()))]
    elements.append(elements[-2])
    
    print('')
    print('Output')
    prev = elements[0]
    for cur in elements[1:]:
        if (prev * cur) > 0:
            print(prev)
        prev = cur

if __name__ == '__main__':
    main()
    sys.exit(0)
        