#!/usr/bin/env python 

import sys

def main():
    s = 'hi'
    print s[1]
    print len(s)
    print s + ' there'
    
    pi = 3.14
    text = 'The value of pi is' + str(pi)
    print text
    
    raw = r'this\t\n and that'
    
    #this\t\n and that
    print raw
    
    multi = """It was the best of times.
    It was the worst of times."""
    
    #It was the best of times.
    #  It was the worst of times.
    print multi
    
    print 'true' if multi.islower() == True else 'false'
    print multi.replace('best', 'good')
    print multi.startswith('It')    

if __name__ == '__main__':
    main()
    sys.exit(0)
    