#!/usr/bin/env python3

import sys
import math

def revsequence():
    a = int(input())
    if a == 0:
        print(a)
        return
    else:
        revsequence()
        print(a)

def main():
    revsequence()

if __name__ == '__main__':
    main()
    sys.exit(0)