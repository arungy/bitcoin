#!/usr/bin/env python

import sys
import math

def main():
    print('Enter the value')
    N = int(input())

    sum = 0
    for i in range(1, N+1):
        sum += i
        
    val = 0
    for i in range(1, N):
        v = int(input())
        val += v
        
    print('The lost card no is', (sum - val))

if __name__ == '__main__':
    main()
    sys.exit(0)
