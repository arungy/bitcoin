#!/usr/bin/python -tt

import sys;

def main():
    val1 = int(input('Enter the first value: '))
    val2 = int(input('Enter the second value: '))
    
    product = val1 * val2

    if product > 1000:
        return val1 + val2
    else:
        return product

if __name__ == '__main__':
    print('Product or Sum of two values: %d' % (main()))
    sys.exit(0)


