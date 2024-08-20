#!/usr/bin/env python

import sys

def main():
    print('Enter two values A & B:')
    A = int(input())
    B = int(input())
    
    if (A <= B):
        v0 = A
        v1 = B
    else:
        v0 = B
        v1 = A
    
    for i in range(v0, v1+1):
        print(i)
        
if __name__ == '__main__':
    main()
    sys.exit(0)
