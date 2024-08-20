#!/usr/bin/python

import sys

def main():
    guest_lists = ['ambita bachan', 'rajini', 'suriya']
    
    print(guest_lists[0].title() + " Bhai... Welcome to this party.")
    print(guest_lists[1].title() + " Thaliva! Tell us one punch dialogue.")
    print(guest_lists[2].title() + " Anna! Give us tips for body building.")
    
if __name__ == '__main__':
    main()
    sys.exit(0)
