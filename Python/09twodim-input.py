#!/usr/bin/env python3

import sys
import math

def twodim_input():
    ##version 1
    #print('enter the number of entries: ')
    #n = int( input() )
    #print("\n" + 'enter the number of entries: ')
    #a = []
    #for i in range(n):
    #    a.append([int(j) for j in input().split()])
        
    #version 2
    print('enter the number of entries: ')
    n = int( input() )
    print("\n" + 'enter the number of entries: ')
    a = [[int(j) for j in input().split()] for i in range(n)]

def main():
    twodim_input()

if __name__ == '__main__':
    main()
    sys.exit(0)
