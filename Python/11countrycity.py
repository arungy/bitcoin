#!/usr/bin/python

import sys
import math

def main():
    print('Enter the number of entry:', end=' ')
    N = int(input())

    Countries = dict()
    for i in range(0, N):
        ln = str(input())
        ln = ln.split()
        Countries[ln[0]] = ln[1:]

    print("\n" + 'Enter the number of city entries:', end=' ')
    M = int(input())

    cities = [str(input()) for j in range(0, M)]

    print()
    for city in cities:
        for key in Countries:
            if city in Countries[key]:
                print(city + " is in " + key)
                break
            #else:          
            #    print(city + " is ** Unknown **")


if __name__ == '__main__':
    main()
    sys.exit(0)


