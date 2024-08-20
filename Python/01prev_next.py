#!/usr/bin/env python3

import sys
import math

def main():
    print('Hello world!\n')

    #reading input from command
    no = int(input())

    print('The next number for the number', no, 'is', str(no+1))
    print('The previous number for the number', no, 'is', str(no-1))

if __name__ == '__main__':
    main()
    sys.exit(0)
 
