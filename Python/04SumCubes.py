#!/usr/bin/env python

import sys

def main():
    print('Enter the value')
    N = int(input())

    sum = 0
    for i in range(0, N+1):
        val = i * i * i
        sum += val

    print('Sum of', N, 'cube values are', sum)
        
if __name__ == '__main__':
    main()
    sys.exit(0)
