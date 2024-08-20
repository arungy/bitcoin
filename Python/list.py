#!/usr/bin/env python

import sys

def main():
    colors = ['red', 'blue', 'green']
    print colors[0]  ## red
    print colors[2]  ## green
    print len(colors) ## 3
    
    b = colors
    print b[1] ## blue
    
    print
    squares = [1, 4, 9, 16]
    sum = 0
    for num in squares:
        sum += num
    print sum   ##30
    
    list = ['larry', 'curly', 'moe']
    if 'curly' in list:
        print 'yay'
        
    ## print the numbers from 0 to 99
    for i in range(100):
        print i
        
    #list methods
    print
    list.append('shemp')
    list.insert(0, 'xxx')
    list.extend(['yyy', 'zzz'])
    print list
    print list.index('curly')
    
    print
    listN = [1, 2, 3]
    print list.append(4)  
    listN.append(4)
    print listN
    
    ##list buildup
    print
    listnew = []
    print listnew
    listnew.append('a')
    listnew.append('b')
    print listnew
    
    ##list slices
    print
    list_slice = ['a', 'b', 'c', 'd']
    print list_slice[1:-1]
    list_slice[0:2] = 'z'
    print list_slice

if __name__ == '__main__':
    main()
    sys.exit(0)