#!/usr/bin/python

import sys

def main():
    squares = [ (value ** 2) for value in range(1, 11)]
    print(squares)
    
    print("min:", min(squares))
    print("max:", max(squares))
    print("sum:", sum(squares))
    
if __name__ == '__main__':
    main()
    sys.exit(0)
