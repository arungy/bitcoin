#!/usr/bin/env python3

import sys
import math

def twodim_array(*wd):
    print('#version 1 (initial)')
    for i in range(len(wd)):
        for j in range(len(wd[i])):
            print(wd[i][j], end=' ')
        print()
    
    print("\n" + '#version 2')
    for row in wd:
        for elem in row:
            print(elem, end=' ')
        print()    

    print("\n" + '#version 3')
    nw = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    s = 0
    for i in range(len(nw)):
        for j in range(len(nw[i])):
            s += nw[i][j]
    print(s)
    
    
    print("\n" + '#version 4')
    nw = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    s = 0
    for row in nw:
        for elem in row:
            s += elem 
    print(s)


def main():
    w = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    twodim_array(w)

if __name__ == '__main__':
    main()
    sys.exit(0)
