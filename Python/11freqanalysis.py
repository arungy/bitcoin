#!/usr/bin/python

import sys
import math

def main():
    print('Enter the number of lines:', end=' ')
    N = int(input())

    allwords = dict()
    for i in range(0, N):
        ln = str(input()).split()

        for wd in ln:
            if wd in allwords:
                allwords[wd] += 1
            else:
                allwords[wd] = 1
   
    for key, val in allwords.items():
        if val in allwords.values():
            print(val, allwords(val).get)


if __name__ == '__main__':
    main()
    sys.exit(0)


