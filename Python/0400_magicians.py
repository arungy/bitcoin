#!/usr/bin/python

import sys

def main():
    magicians = ['david', 'alice', 'carolina']
    
    for magician in magicians:
        print(magician.title() + ", that was a great trick!")
        print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
    print("Thank you, everyone. That was a great magic show!")
    
if __name__ == '__main__':
    main()
    sys.exit(0)
