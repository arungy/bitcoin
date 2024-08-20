"""Retrive data in JSON format"""

import sys
import json

def main():
    filename = 'numbers.json'

    with open(filename) as fp:
        numbers = json.load(fp)

    print(numbers)

if __name__ == '__main__':
    main()
    sys.exit(1)
