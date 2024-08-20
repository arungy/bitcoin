#!/usr/bin/env python

import sys

def repeat(s, exclaim):
    """
    Return the string 's' repeated 3 times.
    If exclaim is true, add exclamation mark.
    """
    
    result = s + s + s
    if exclaim:
        result = result + '!!!'
    return result
    
def main():
    print repeat('Yay', False)
    print repeat('Woo Hoo', True)
    
if __name__ == '__main__':
    main()
    #help(len)
    #help(sys)
    #dir(list)
    help(list)
    sys.exit(0)