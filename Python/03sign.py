#!/usr/bin/env python3

import sys

def main():
    x = int(input())

    if x > 0:
        print('1')
    elif x < 0:
        print('-1')
    else:
        print('0')

if __name__ == '__main__':
    main()
    sys.exit(0)
