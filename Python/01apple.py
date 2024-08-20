#!/usr/bin/env python3

import sys
import math

def main():
    print('Hello world!\n')

    #reading input from command
    N = int(input())
    k = int(input())

    print('Single student will get', int(N/k), 'apple', '& Reamining apple is', (N%k))

if __name__ == '__main__':
    main()
    sys.exit(0)
 
