#!/usr/bin/pthon

import sys

def main():
    print('Enter number of elements')
    elements = [int(input()) for i in range(int(input()))]
    
    large = elements[0]
    for cur in elements[1:]:
        if cur > large:
            large = cur
    
    print("\nLargest value:", large, "Index:", elements.index(large))
    
    
if __name__ == '__main__':
    main();
    sys.exit(0)
    