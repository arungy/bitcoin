#!/usr/bin/python -tt

import sys;

def divisible_by5():
    print('Enter the sentence: ')
    sentence = input()
    senlist = sentence.split()

    print('Enter the sub-string to count: ')
    substr = input().strip()

    #method 1
    count = 0
    for w in senlist:
        if substr == w:
            count += 1

    print('1. Number of \'%s\' occurance in \'%s\' is: %d' % (substr, sentence, count))

    #method 2
    print('2. Number of \'%s\' occurance in \'%s\' is: %d' % (substr, sentence, sentence.count(substr)))

def main():
    divisible_by5()

if __name__ == '__main__':
    main()
    sys.exit(0)


