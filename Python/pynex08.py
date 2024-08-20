#!/usr/bin/python -tt

import sys;

def divisible_by5():
    print('Enter the number: ')
    N = int(input())

    for c in range(1, N+1):
        for x in range(0, c):
            print(c, end = " ")
        print()

def main():
    divisible_by5()

if __name__ == '__main__':
    main()
    sys.exit(0)


