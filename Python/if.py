#!/usr/bin/env python

import sys

def write_ticket():
    print "Your ticket is on the way"

def main():
    speed = 0
    mood = ""
    
    len_argv = len(sys.argv)
    if  len_argv >= 2 :
        if sys.argv[1] == "": speed = 100
        else: speed = int(sys.argv[1])
    
    if len_argv >= 3:
        if sys.argv[2] == "": mood = 'good' 
        else: mood = sys.argv[2]
    
    print speed
    if speed >= 80:
        print "Licence and registration please"
        if mood == 'terrible' or speed >= 100:
            print "You have the right to remain silent."
        elif mood == 'bad' or speed >= 90:
            print "I'm going to have to write you a new ticket."
            write_ticket()
        else:
            print "Let's try to keep it under 80 ok?"
    
    
if __name__ == '__main__':
    main()
    sys.exit(0)
    