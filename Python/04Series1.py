#!/usr/bin/env python

import sys

def main():
    print('Enter two values A & B:')
    A = int(input())
    B = int(input())
    
    if (A > B):
        T = A
        A = B
        B = T
    
    for i in range(A, B+1):
        print(i)
        
if __name__ == '__main__':
    main()
    sys.exit(0)
