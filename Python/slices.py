#!/usr/bin/env python

import sys

def main():
    print 'main'
    
    s = "Hello"
    print s[1:4]
    print s[1:]
    print s[:]
    print s[1:100]
    
    print
    print s[-1]
    print s[-4]
    print s[-3:]
    
    #Strings %
    text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blown your %s down." % (3, 'huff', 'puff', 'house')  #one way using % operator
    print text
    
    text = (
        "%d little pigs come out, or I'll %s, and I'll %s, and I'll blown your %s down." 
        % (3, 'huff', 'puff', 'house'))  #other way using % operator
    print text
    
    text = (
        "%d little pigs come out,"
        " or I'll %s, and I'll %s,"
        " and I'll blown your %s down." 
        % (3, 'huff', 'puff', 'house'))  #another way using % operator
    print text
    
    #check out heavily "unicode" support for strings
    
if __name__ == '__main__':
    main()
    
    sys.exit(0)
    