#!/usr/bin/python

import sys
import math

def main():
    print('enter the line: ')
    line = str(input())
    words = line.split()

    wordcnt = dict()
    for word in words:
        if word in wordcnt:
            wordcnt[word] = wordcnt[word] + 1
        else:
            wordcnt[word] = 0
        print(wordcnt[word], end=' ')



if __name__ == '__main__':
    main()
    sys.exit(0)

