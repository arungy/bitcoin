#!/usr/bin/python

import sys
import math

def main():
    print('Enter the number of files:', end=' ')
    N = int(input())

    filesystem = [str(input()) for i in range(0, N)]

    fsdict = dict()
    for i in range(0, N):
        ef = filesystem[i].split()
        fsdict[ef[0]] = ef[1:]

    print("\n" + 'Enter the number of operational files:', end=' ')
    M = int(input())

    operfiles = [str(input()) for j in range(0, M)]

    print()
    for f in operfiles:
        of = f.split()

        fname = of[1].lower()
        foper = of[0].lower()

        if foper == "read":
            foper = "R"
        elif foper == "write":
            foper = "W"
        elif foper == "execute":
            foper = "X"

        if foper in fsdict[fname]:
            print(f + ": OK")
        else:
            print(f + ": Access Denied")


if __name__ == '__main__':
    main()
    sys.exit(0)


