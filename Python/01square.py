#!/usr/bin/env python3

import sys

def main():
    print('Hello world!\n')

    #reading input from command
    val0 = int(input())
    val1 = int(input())

    print('square:', (val0 ** val1))

if __name__ == '__main__':
    main()
    sys.exit(0)
 
