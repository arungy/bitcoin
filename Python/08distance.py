#!/usr/bin/env python3

import sys
import math

def distance(x1, y1, x2, y2):
    return math.sqrt( math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2) )

def main():
    print('Inside main')
    print('enter x1 & x2 value:')
    x1 = float(input())
    y1 = float(input())
    
    print('enter y1 & y2 value:')
    x2 = float(input())
    y2 = float(input())
    
    print('distacnce(%d, %f, %d, %f): %f' % (x1, y1, x2, y2, distance(x1, y1, x2, y2)))


if __name__ == '__main__':
    main()
    sys.exit(0)