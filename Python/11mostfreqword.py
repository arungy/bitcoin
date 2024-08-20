#!/usr/bin/python

import sys
import math

def main():
    print('Enter the number of lines:', end=' ')
    N = int(input())

    lines = [str(input()) for i in range(N)]

    mostfreqs = dict()
    for i in range(0, N):
        line = lines[i].split()

        for wd in line:
            if wd in mostfreqs:
                mostfreqs[wd] += 1
            else:
                mostfreqs[wd] = 1

    print(max(sorted(mostfreqs), key=mostfreqs.get))


if __name__ == '__main__':
    main()
    sys.exit(0)

