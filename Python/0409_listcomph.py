#!/usr/bin/python

import sys

def main():
    cubes = [(value ** 3) for value in range(1, 11)]
    print(cubes)

if __name__ == '__main__':
    main()
    sys.exit(0)