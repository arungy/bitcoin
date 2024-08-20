#!/usr/bin/python

import sys

def main():
    my_fruits = ['mango', 'grapes', 'apple', 'jack fruit', 'guava', 'water melon']
    
    print("The first three items in the list are:", my_fruits[0:3])
    print("Three items from the middle of the list are:", my_fruits[2:5])
    print("The last three items in the list are:", my_fruits[-3:])
   

if __name__ == '__main__':
    main()
    sys.exit(0)