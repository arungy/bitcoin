#!/usr/bin/python

import sys

def main():
    guest_lists = ['senthil', 'raj', 'ameen']
    
    #print("Hi " + guest_lists[0].title() + ", We coridally invite you for my House Warming Dinner Party.")
    #print("Hi " + guest_lists[1].title() + ", We coridally invite you for my House Warming Dinner Party.")
    #print("Hi " + guest_lists[2].title() + ", We coridally invite you for my House Warming Dinner Party.")
    
    print("Hi Everybody, " + guest_lists[0].title() + " could not come to Party due to some other urgent work.")
    del guest_lists[0]
    
    print("")
    print("Hi " + guest_lists[0].title() + ", We coridally invite you for my House Warming Dinner Party.")
    print("Hi " + guest_lists[1].title() + ", We coridally invite you for my House Warming Dinner Party.")
    
if __name__ == '__main__':
    main()
    sys.exit(0)
