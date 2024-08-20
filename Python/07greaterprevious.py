#!/usr/bin/pthon

import sys

def main():
    print('Enter number of elements')
    elements = [int(input()) for i in range(int(input()))]
    
    prev = elements[0]
    for cur in elements[1:]:
        if cur > prev:
            print(cur)
        prev = cur
    
if __name__ == '__main__':
    main();
    sys.exit(0)
    