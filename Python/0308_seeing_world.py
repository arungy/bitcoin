#!/usr/bin/python

import sys

def main():
    places = ['himalaya', 'taj mahal', 'kasi', 'rameswaram', 'tanjavur']
    
    print("Original list:", places)
    
    print("Sorted list:", sorted(places))
    
    print("Original list again:", places)
    
    print("Reverse Sorted list:", sorted(places, reverse=True))
    
    print("Original list again:", places)
    
    print()
    places.reverse()
    print('Reversed list:', places)
    
    places.reverse()
    print('Reversed to Original list order:', places)
    
    print()
    places.sort()
    print('Sorted list', places)
    
    places.sort(reverse=True)
    print('Reverse using sorted list:', places)
    
if __name__ == '__main__':
    main()
    sys.exit(0)
