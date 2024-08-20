#!/usr/bin/env python3

import sys

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i

    return res

def max(a, b):
    if a > b :
        return a
    else:
        return b

def max3(a, b, c):
    return max(max(a, b), c)
    
def max(*a):
    res = a[0]
    for val in a[1:]:
        if val > res:
            res = val
    
    return res
    


def main():
    print('Inside main')
    print('fact(4): %d' % factorial(4))
    
    print("max: %d" % max(3, 5))
    print("max: %d" % max(5, 3))
    #print("max: %d" % max(int(input()), int(input())))
    #print("max3: %d" % max3(int( input() ), int( input() ), int( input() ) ))
    print("new max: %d" % max(2, 7, 4))


if __name__ == '__main__':
    main()
    sys.exit(0)