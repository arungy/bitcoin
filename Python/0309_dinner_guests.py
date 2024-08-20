#!/usr/bin/python

import sys

def main():
    guest_lists = ['senthil', 'raj', 'ameen']
 
    guest_lists.insert(0, 'naveen')
    guest_lists.insert(2, 'prabhu')
    guest_lists.append('ragu')

    print('lenght of list:', len(guest_lists))
    
if __name__ == '__main__':
    main()
    sys.exit(0)
