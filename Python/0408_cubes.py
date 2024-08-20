#!/usr/bin/python

import sys

def main():
    values = []
    
    for value in range(1, 11):
        values.append(value ** 3)
        
    for value in values:
        print(value, end='  ')
     
    
if __name__ == '__main__':
    main()
    sys.exit(0)
