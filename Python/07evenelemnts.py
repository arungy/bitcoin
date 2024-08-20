#!/usr/bin/pthon

import sys

def main():
    print('Enter number of elements')
    elements = [int(input()) for i in range(int(input()))]
    
    for i in elements:
        if i % 2 == 0:
            print(i)
    
    
if __name__ == '__main__':
    main();
    sys.exit(0)
    