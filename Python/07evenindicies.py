#!/usr/bin/pthon

import sys

def main():
    print('Inside main')
    
    newitems = []
    print('Enter the number of elements:')
    n = int(input())
    
    for i in range(int(n)):
        str = input()
        newitems.append(str)
    print('')
    
    print(newitems[::2])
        
    
    
if __name__ == '__main__':
    main();
    sys.exit(0)
    