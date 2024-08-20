#!/usr/bin/env python

import sys

def listex0():
    Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet' ]
    print(Rainbow[0])
    print('')
    
    Rainbow[0] = 'red'
    print('print the Rainbow')
    for i in range(len(Rainbow)):
        print(Rainbow[i])
        
def listex0():
    i = 0
    a = []
    print('Enter num of elements:')
    n = int(input())
    
    print('Enter each element:')
    for i in range(n):
        new_element = int(input())
        a.append(new_element)
    
    print(a)

def listex2():
    a = [1, 2, 3]
    b = [4, 5]
    c = a + b
    d = b * 3
    print(c)
    print(d)
    print([7, 8] + [9])
    print([0, 1] * 3)
    
def listex3():
    print('')
    print('Enter num of element:')
    a = [0] * int(input())
    for i in range(len(a)):
        a[i] = int(input())
    print(a)  


def listex4():
    a = [0, 1, 2, 3, 4, 5]
    
    for i in range(len(a)):
        print(a[i])
        
    #for elem in a:
    #    print(elem, end=' ')


def listex5():
    s = 'ab12c59p7dq'
    digits = []
    
    for symbol in s:
        if '1234567890'.find(symbol) != -1:
            digits.append(int(symbol))
    
    print(digits)
    
    #s = input()
    #a = s.split()
    #print(a)
    
    #print('')
    #print('Enter the elements:')
    #a = input().split()
    #for i in range(len(a)):
    #    a[i] = int(a[i])
    #print(a)
    
    #a = [int(s) for s in input().split()]
    #print(a)
    
    a = '43.88.64.10'.split('.')
    print(a)
    
    a = ['red', 'green', 'blue']
    print(' '.join(a))
    print('***'.join(a))
    
    a = [1, 2, 3]
    print(' '.join([str(i) for i in a]))
    

def main():
    print('Inside main')
    
    #listex0()
    #listex1()
    #listex2()
    #listex3()
    #listex4()
    listex5()

if __name__ == '__main__':
    main()
    sys.exit(0)
    
