#!/usr/bin/python -tt

import sys;

def reverse_int():
    print('Enter the number: ')
    num = int(input())

    while (num > 0):
        rem = num % 10
        num = num // 10
        print(rem, end = " ")

def main():
    reverse_int()

if __name__ == '__main__':
    main()
    sys.exit(0)


