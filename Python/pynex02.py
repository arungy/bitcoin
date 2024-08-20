#!/usr/bin/python -tt

import sys;

def main():
    prevnum = 0
    N = int(input('Enter the range value: '))
   
    for curnum in range(0, N):
        sumval = prevnum + curnum
        print('prev num: %d, curr num: %d, sum (prev + curr): %d' % (prevnum, curnum, sumval))
        prevnum = curnum

if __name__ == '__main__':
    main()
    sys.exit(0)


