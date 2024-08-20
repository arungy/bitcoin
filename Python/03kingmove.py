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

    if ((mx == 0 or mx == 1 or mx == -1) and (my == 0 or my == 1 or my == -1)):
        print('YES')
    else:
        print('NO')
        
if __name__ == '__main__':
    main()
    sys.exit(0)
