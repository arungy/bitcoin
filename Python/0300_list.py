#!/usr/bin/python

import sys

def main():
    bicycles = ['trek', 'cannondale', 'redline', 'specalized']
    
    for i in range(0, len(bicycles), 1):
        message = "My " + str(i + 1) + "st bicycle is " + bicycles[i].title() + "."
        print(message)
    

if __name__ == '__main__':
    main()
    sys.exit(0)
