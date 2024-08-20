#!/usr/bin/env python

import sys
import re

def repetition():
    ## i+ = one or more i's as many as possible
    print
    print 'repetition()'
    match = re.search(r'pi+', 'piiig')
    print match.group() 
    
    ## Find the first/leftmost solution, and within it drives the +
    ## as far as possible (aka 'leftmost and largest')
    ## In this example, note that it does not get to the second of i's.
    match = re.search(r'i+', 'piigiiii')
    print match.group()
    
    ## \s* = zero or more whitespace chars
    ## Here look for 3 digits, possibly seperated by whitespace.
    match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
    print match.group()
    match = re.search(r'\d\s*\d\s*\d', 'xx12   3xx')
    if match: print match.group()
    
    match = re.search(r'\d\s*\d\s*\d', 'xx123xxx')
    if match: print match.group()
    
    ## ^ = matches the start of string, so that fails:
    print
    match = re.search(r'^b\w+', 'foobar')
    if match: print match.group()
    ## but without the ^ it succeeds:
    match = re.search(r'b\w+', 'foobar')
    if match: print match.group()
    
def re_emails():
    str = 'purple alice-b@google.com monkey dishwasher'
    match = re.search(r'\w+@\w+', str)
    if match: print match.group()
    
    match = re.search(r'[\w-]+@[\w.]+', str)
    if match: print match.group()
    
    ##Group extraction
    print
    match = re.search(r'([\w-]+)@([\w.]+)', str)
    if match: print match.group()
    if match: print match.group(1)
    if match: print match.group(2)

def re_findall():
    print
    f = open('test.txt', 'r')
    #strings = re.findall('some pattern', f.read())
    strings = re.findall('findall', f.read())
    for s in strings:
        print s #strings
    f.close()
    
def re_findall_group():
    str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
    tuples = re.findall(r'([\w\.-]+)@([\w.-]+)', str)
    print tuples
    for tuple in tuples:
        print tuple[0]
        print tuple[1]
    
    print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
    
def main():
    str = 'an example word:cat!!'
    match = re.search(r'word:\w\w\w', str)
    if match:
        print match.group()
    else:
        print 'not found'
    
    ## Search for pattern 'iii' in string 'piig'
    ## All of the pattern must match, but it may appear anywhere.
    ## On success, match.group() is matched text
    print
    match = re.search(r'iii', 'piiig')
    print match.group()
    match = re.search(r'igs', 'piiig')
    if not match:
        print 'not found'
        
    ##. = any char expect \n
    match = re.search(r'..g', 'piiig')
    print match.group()
    
    ##\d = digit char, \w = word char
    print
    match = re.search(r'\d\d\d', 'p123g')
    print match.group()
    match = re.search(r'\w\w\w', '@@abcd!!')
    print match.group()
    
    repetition()
    re_emails()
    re_findall()
    re_findall_group()
    
if __name__ == '__main__':
    main()
    sys.exit(0)