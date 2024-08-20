#!/usr/bin/env python

import sys

def main():
    N = int(input())
    print('Enter the', N, 'values')

    sum = 0
    for i in range(0, N):
        val = int(input())
        sum += val

    print('Sum of', N, 'values is', sum)
        
if __name__ == '__main__':
    main()
    sys.exit(0)
