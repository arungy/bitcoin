#!/usr/bin/python -tt

import sys;

def print_form_table():
    print('Enter the element to print the table: ')
    N = int(input())

    for n in range(1, N+1):
        for i in range(1 , 11):
            print((i * n), end=" ")
        print("")


def main():
   print_form_table()

if __name__ == '__main__':
    main()
    sys.exit(0)


