#!/usr/bin/python -tt

import sys;

def same_list():
    print('Enter the num of elements: ')
    N = int(input())

    listval = []
    print('Enter the elements: ')
    for i in range(N):
        listval.append(int(input()))

    print("Given list is ", listval)
    if listval[0] == listval[-1]:
        print('result is True')
    else:
        print('result is False')


def main():
    same_list()

if __name__ == '__main__':
    main()
    sys.exit(0)


