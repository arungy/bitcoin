#!/usr/bin/python

import sys

def main():
    guest_lists = ['senthil', 'raj', 'ameen']

    print("Hi Everyone! I found a bigger dinner table. I would like to invite more people for Dinner.")
    
    guest_lists.insert(0, 'naveen')
    guest_lists.insert(2, 'prabhu')
    guest_lists.append('ragu')

    print("")
    print("Hi " + guest_lists[0].title() + ", We coridally invite you to my House Warming Party.")
    print("Hi " + guest_lists[1].title() + ", We coridally invite you to my House Warming Party.")
    print("Hi " + guest_lists[2].title() + ", We coridally invite you to my House Warming Party.")
    print("Hi " + guest_lists[3].title() + ", We coridally invite you to my House Warming Party.")
    print("Hi " + guest_lists[4].title() + ", We coridally invite you to my House Warming Party.")
    print("Hi " + guest_lists[5].title() + ", We coridally invite you to my House Warming Party.")

if __name__ == '__main__':
    main()
    sys.exit(0)
