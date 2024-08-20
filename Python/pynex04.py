#!/usr/bin/python -tt

import sys;

def remove_char():
    strg = input('Enter the string: ')
    N = int(input('Enter the position: '))
    L = len(strg)
  
    if N < L:
        print(strg[N:])
    else:
        print('error: \'Position\' must be lesser than String length')

def main():
    remove_char()

if __name__ == '__main__':
    main()
    sys.exit(0)


