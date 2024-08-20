#!/usr/bin/env python3

import sys

def main():
    print('Exter the position x0 & y0:')
    x0 = int(input())
    y0 = int(input())

    print('Exter the position x1 & y1:')
    x1 = int(input())
    y1 = int(input())

    px = ((x1 % 2) == 0) == ((x0 % 2) == 1)
    py = ((y1 % 2) == 0) == ((y0 % 2) == 1)

    if (px == True and py == True):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
    sys.exit(0)
