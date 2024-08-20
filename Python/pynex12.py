#!/usr/bin/python -tt

import sys;

def calc_income_tax():
    print('Enter the amount to calculate the tax: ')
    amount = int(input())

    tax = 0
    if amount < 10000:
        tax = 0
    elif amount < 20000:
        tax = (amount - 10000) * (10 / 100)
    else:
        #first 10000
        tax = 0

        #next 10000
        tax += (10000 * (10 / 100))

        #remaining amount
        tax += ((amount - 20000) * (20 / 100))

    print('The tax of $%d is :$%d' % (amount, tax)) 


def main():
   calc_income_tax()

if __name__ == '__main__':
    main()
    sys.exit(0)


