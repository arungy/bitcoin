#!/usr/bin/python

import sys

def main():
    guest_lists = ['senthil', 'raj', 'ameen']
 
    guest_lists.insert(0, 'naveen')
    guest_lists.insert(2, 'prabhu')
    guest_lists.append('ragu')

    print()
    removed_person = guest_lists.pop()
    print("Sorry " + removed_person.title() + ", I can't invite you for the dinner.")
    
    removed_person = guest_lists.pop()
    print("Sorry " + removed_person.title() + ", I can't invite you for the dinner.")
    
    removed_person = guest_lists.pop()
    print("Sorry " + removed_person.title() + ", I can't invite you for the dinner.")
    
    removed_person = guest_lists.pop()
    print("Sorry " + removed_person.title() + ", I can't invite you for the dinner.")
    
    print()
    print("Hi " + guest_lists[0].title() + ", We coridally invite you to my House Warming Party.")
    del guest_lists[0]
    
    print("Hi " + guest_lists[0].title() + ", We coridally invite you to my House Warming Party.")
    del guest_lists[0]
    
if __name__ == '__main__':
    main()
    sys.exit(0)
