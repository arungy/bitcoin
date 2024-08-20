#!/usr/bin/env python3

import sys

def main():
    print('Hello world!\n')

    #reading input from command
    val0 = input()
    val1 = input()
    val2 = input()
    
    s = val0 + val1
    sv = int(val0) + int(val1)
    s3 = int(val0) + int(val1) + int(val2)

    print('val0 + val1:', s)
    print('int(val0) + int(val1): ', sv)
    print('int(val0) + int(val1) + int(val2): ', s3)


if __name__ == '__main__':
    main()
    sys.exit(0)
 
