#!/usr/bin/python -tt

import sys;

def odd_list():
    print('Enter the first list: ')
    firstlist = input().split()
    
    print('Enter the second list: ')
    secondlist = input().split()

    odd_list = []
    for x in firstlist:
        ix = int(x)
        if ix % 2 != 0:
            odd_list.append(ix)

    for x in secondlist:
        ix = int(x)
        if ix % 2 == 0:
            odd_list.append(ix)

    print("Given first list:", firstlist)
    print("Given second list:", secondlist)

    print("Extracting odd numbers from 1st and 2nd list:", odd_list)

def main():
    odd_list()

if __name__ == '__main__':
    main()
    sys.exit(0)


