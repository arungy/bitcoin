#!/usr/bin/env python3

import sys
import math

def nested_list():
    print('#version 1')
    m = 5
    n = 3
    a = [ [0] * m] * n
    a[0][0] = 5
    print(a[1][0])
    
    print('#version 2 (possiblity 1)')
    a = [0] * n
    for i in range(0, n):
        a[i] = [0] * m

    print('#version 2 (possiblity 2)')
    for i in range(0, n):
        a.append([0] * m)

    print('#version 2 (possiblity 3)')
    a = [ [0] * m for i in range(n)]

def main():
    nested_list()

if __name__ == '__main__':
    main()
    sys.exit(0)
