#!/usr/bin/env python3

import sys
import math

def set_guess():
    print('Enter the number of element: ')
    n = int( input() )
    
    A = set([x for x in range(1, n + 1)])
    
    while(1):
        print('Enter the Beatrice guess: ')
        inp = input()
        
        if inp == 'help' or inp == 'HELP':
            D = A.difference(B)
            print(' '.join([str(e) for e in sorted(D)]))
            return 0
            
        else:
            B = set([int(x) for x in inp.split()])
            C = A & B
    
            if sorted(C) == sorted(B):
                print('YES')
            else:
                print('NO')


def main():
    set_guess()

if __name__ == '__main__':
    main()
    sys.exit(0)
