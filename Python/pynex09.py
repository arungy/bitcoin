#!/usr/bin/python -tt

import sys;

def reverse_num():
    print('Enter the number: ')
    strg = input()

    #method 1
    if strg == strg[::-1]:
        print('The original and reverse number is the same')
    else:
        print('The original and reverse number is not the same')

    #methodd 2
    fwdnum = int(strg)

    num = fwdnum
    revnum = 0
    while (num > 0):
        rem = num % 10
        revnum = (revnum * 10) + rem
        num = num // 10

    if fwdnum == revnum:
        print('The original and reverse number is the same')
    else:
        print('The original and reverse number is not the same')




def main():
    reverse_num()

if __name__ == '__main__':
    main()
    sys.exit(0)


