#!/usr/bin/python

import sys

def main():
    values = list(range(3, 31, 3))
    
    for value in values:
        print(value, end=' ')
    
if __name__ == '__main__':
    main()
    sys.exit(0)
