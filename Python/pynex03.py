#!/usr/bin/python -tt

import sys;

def even_char():
    val = input("Enter the string: ")
   
    for n in range(0, len(val) -1, 2):
        print(val[n])

def main():
    even_char()

if __name__ == '__main__':
    main()
    sys.exit(0)


