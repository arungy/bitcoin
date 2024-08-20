#!/usr/bin/env python

import sys

def main():
    print('Enter the value')
    N = int(input())

    for i in range(1, N+1):
        for j in range(1, i+1):
            print(j, sep='', end='')
        print(end='\n')

if __name__ == '__main__':
    main()
    sys.exit(0)
