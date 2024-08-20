#!/usr/bin/env python3

import sys
import math

def capitalize(wd):
    
    nw = ''
    flag = 0
    
    for i in range(0, len(wd), 1):
        c = wd[i]
        if i == 0 or flag == 1:
            c = chr(ord(c) - 32)
            flag = 0
            
        if c == ' ':
            flag = 1
        nw = nw + c
        
    return nw

def main():
    print('Enter the word:')
    w = input()
    print('capitalize(%s): %s' % (w, capitalize(w)))
    

if __name__ == '__main__':
    main()
    sys.exit(0)
