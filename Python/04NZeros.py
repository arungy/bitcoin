#!/usr/bin/env python

import sys

def main():
    print('Enter the value')
    N = int(input())

    sum = 0
    for i in range(1, N+1):
        val = int(input())
        if val == 0:
            sum += 1

    print('Number of Zeros in', N, 'given number is', sum)
        
if __name__ == '__main__':
    main()
    sys.exit(0)
