#!/usr/bin/env python

import sys

def main():
    print('Enter the value')
    N = int(input())

    sum = 1
    for i in range(1, N+1):
        sum *= i

    print('Sum of', N, 'factorial is', sum)
        
if __name__ == '__main__':
    main()
    sys.exit(0)
