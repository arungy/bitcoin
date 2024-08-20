#!/usr/bin/env python

import sys

def main():
    print('>_< ' * 5)
    print(len('abcdefghijklmnopqrstuvwxyz'))
    
    s = str(2 ** 100)
    print(s)
    print(len(s))
    
    S = 'Hello'
    print(S[0:4])
    print(S[:-3])

    #subsequence
    s = 'abcdefghijklm'
    print(s[1:10:2])
    for i in range(1, 10, 2):
        print(i, s[i])

    print(s.find('e'))
    print(s.find('gh'))
    print(s.find('L'))
    print()

    s = 'abracadabra'
    print(s.find('b'))
    print(s.rfind('b'))
    print()

    s = 'my name is bond, james bond, okay?'
    print(s.find('bond'))
    print(s.find('bond', 12))
    print()

    print('a bar is a bar, essentially'.replace('bar', 'pub'))
    print()
    
    print('a bar is a bar, essentially'.replace('bar', 'pub', 1))
    print()
  
    print('Abracadabra'.count('a'))
    print('aaaaaaaaaa'.count('aaa'))
    print()

if __name__ == '__main__':
    main()
    sys.exit(0)
