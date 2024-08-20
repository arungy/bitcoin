#!/usr/bin/env python3

import sys
import math

def twodim_example():
    n = 5
    a = [[0] * n for i in range(n)]
    
    #version 1
    for i in range(n):
        for j in range(n):
            if i < j:
                a[i][j] = '0'
            elif i > j:
                a[i][j] = '2'
            else:
                a[i][j] = '1'
    
    for row in a:
        print(' '.join([str(elem) for elem in row]))
        
    #version 2
    print("\n" + 'version 2')
    a2 = [[0] * n for i in range(n)]

    for i in range(n):
        a2[i] = [2] * i + [1] + [0] * (n - i - 1)

    for row in a2:
        print(' '.join([str(elem) for elem in row]))
    
    #version 3
    print("\n" + 'version 3')
    a3 = [[0] * n for i in range(n)]
    
    a3 = [[2] * i + [1] + [0] * (n - i - 1) for i in range(n)]
    
    for row in a3:
        print(' '.join([str(elem) for elem in row]))
        
    #version 4
    x = 5
    y = 6
    
    print("\n" + 'version 4')
    a4 = [[0] * x  for i in range(y)]
    
    a4 = [ [i * j for i in range(x)] for j in range (y)]
    for row in a4:
        print(' '.join([str(elem) for elem in row]))


def main():
    twodim_example()

if __name__ == '__main__':
    main()
    sys.exit(0)
