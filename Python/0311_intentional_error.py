#!/usr/bin/python

import sys

def main():
    guest_lists = ['senthil', 'raj', 'ameen']
 
    guest_lists.insert(0, 'naveen')
    guest_lists.insert(2, 'prabhu')
    guest_lists.append('ragu')

    print('list item:', guest_lists[-1])
    
    new_guests = []
    
    new_guests.append(guest_lists[-2])
    print('new list item:', new_guests[-1])
    
    
if __name__ == '__main__':
    main()
    sys.exit(0)
