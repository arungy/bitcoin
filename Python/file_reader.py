"""A file read the the pi value"""

import sys

def main():
    filename = './pi_digits.txt'
    with open(filename) as fp:
        lines = fp.readlines()
        
    for line in lines:
        print(line.rstrip())

if __name__ == '__main__':
    main()
    sys.exit(1)