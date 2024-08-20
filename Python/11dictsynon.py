#!/usr/bin/python

import sys
import math

def main():
    print('Enter the number of elements:', end=' ')
    N = int(input())

    dicto = dict()
    for i in range(0, N):
        line = str(input()).split()
        dicto[line[0]] = line[1]

    print("\n" + 'Enter the word:', end=' ')
    wd = str(input())

    for key, val in dicto.items():
        if wd == key:
            print('Meaning of "' + wd + '" is ' + val)
        elif wd == val:
            print('Meaning of "' + wd + '" is ' + key)


if __name__ == '__main__':
    main()
    sys.exit(0)

