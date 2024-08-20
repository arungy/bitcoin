#!/usr/bin/python -tt

import sys;

def print_form_table():
    print('Enter the number to print astrik: ')
    N = int(input())

    for n in range(N+1, 1, -1):
        for i in range(1 , n):
            print("*", end=" ")
        print("")


def main():
   print_form_table()

if __name__ == '__main__':
    main()
    sys.exit(0)


