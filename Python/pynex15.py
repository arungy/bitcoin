#!/usr/bin/python -tt

import sys;

def exponent(base, exp):
    proval = 1
    for i in range(exp):
        proval *= base

    return proval

def main():
    base = int(input('enter the base value: '))
    exp = int(input('enter the exponent value: '))
    print ('%d raises to the power of %d is: %d' % (base, exp, exponent(base, exp)))

if __name__ == '__main__':
    main()
    sys.exit(0)


