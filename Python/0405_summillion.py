#!/usr/bin/python

import sys

def main():
    values = list(range(1, 1000001))
    
    print("min:", min(values))
    print("max:", max(values))
    print("sum:", sum(values))
    
if __name__ == '__main__':
    main()
    sys.exit(0)
