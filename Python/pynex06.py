#!/usr/bin/python -tt

import sys;

def divisible_by5():
    print('Enter the num of elements: ')
    N = int(input())

    listval = []
    print('Enter the elements: ')
    for i in range(N):
        listval.append(int(input()))

    print("Given list is", listval)
    print("Divisible by 5 in the list")
    for n in listval:
        if 0 == (n % 5):
            print(n)

def main():
    divisible_by5()

if __name__ == '__main__':
    main()
    sys.exit(0)


