#!/usr/bin/env python3

import sys

def main():
    print('Exter the position x0 & y0:')
    x0 = int(input())
    y0 = int(input())

    print('Exter the position x1 & y1:')
    x1 = int(input())
    y1 = int(input())

    mx = x1 - x0
    my = y1 - y0

    if (((y0 % 2) == 1 and (x0 % 2) == 1) or ((y0 % 2) == 0 and (x0 % 2) == 0)):
        mx = True
    else:
        mx = False
        
    if (((y1 % 2) == 1 and (x1 % 2) == 1) or ((y1 % 2) == 0 and (x1 % 2) == 0)):
        my = True
    else:
        my = False

    if mx == my:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
    sys.exit(0)
