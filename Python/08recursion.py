#!/usr/bin/env python3

import sys

def recursion(n):
    if n == 0:
        return 1
    else:
        return n * recursion(n-1)

def main():
    print('Inside main')
    print('recursion(%d): %d' % (5, recursion(5)))


if __name__ == '__main__':
    main()
    sys.exit(0)