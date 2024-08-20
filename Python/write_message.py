"""An example to write the file"""

import sys

def main():
    filename = 'programming.txt'

    with open(filename, 'a') as fp:
        fp.write("I also love finding meaning in large datasets.\n")
        fp.write("I love creating apps than can run in a browser.\n")

if __name__ == '__main__':
    main()
    sys.exit(1)
