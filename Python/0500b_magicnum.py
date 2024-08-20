#!/usr/bin/python

import sys

def main():
    answer = 17
    
    if answer != 42:
        print("This is not the correct answer. Please try again.")
    
    age_0 = 21
    age_1 = 18
    
    #'and' operator
    print("\nand operation:")
    if (age_0 >= 21) and (age_1 >= 21):
        print('True')
    else:
        print('False')
    
    #'or' operator
    print("\nor operation:")
    if (age_0 >= 21) or (age_1 >= 21):
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()
    sys.exit(0)