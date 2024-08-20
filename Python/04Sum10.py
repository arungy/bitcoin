#!/usr/bin/env python

import sys

def main():
    print('Enter the 10 values:')
    
    sum = 0
    for i in range(0, 10):
        val = int(input())
        sum += val

    print('sum of 10 values:', sum)
        
if __name__ == '__main__':
    main()
    sys.exit(0)
