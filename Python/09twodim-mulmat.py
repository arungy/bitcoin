#!/usr/bin/env python3

import sys
import math

def twodim_mul_matrix():
    print('Enter the number of elemnts: ')
    M = int( input() )
    N = int( input() )
    R = int( input() )
    
    matA = [[1 for x in range(N)] for y in range(M)]
    matB = [[1 for x in range(R)] for y in range(N)]
    matC = [[0 for x in range(R)] for y in range(M)]
    
    print('Enter the element 1: ')
    matA = [[x for x in input().split()] for y in range(M)]
    
    print('Enter the element 2: ')
    matB = [[x for x in input().split()] for y in range(N)]
    
    for y in range(M):
        for x in range(R):
            for n in range(N):
                matC[y][x] += int(matA[y][n]) * int(matB[n][x])
                
    for ele in matC:
        print(' '.join([str(x) for x in ele]))

def main():
    twodim_mul_matrix()

if __name__ == '__main__':
    main()
    sys.exit(0)
