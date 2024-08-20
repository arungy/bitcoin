#!/usr/bin/env python

import sys

def main():
    print('Enter the value')
    N = int(input())

    sum = 0
    val = 1
    for i in range(1, N+1):
        val *= i
        sum += val

    print('Sum of', N, 'added factorial is', sum)
        
if __name__ == '__main__':
    main()
    sys.exit(0)
