"""Store data in JSON format"""

import sys
import json

def main():
    numbers = [i * 2 for i in range(0, 5)]

    filename = 'numbers.json'
    with open(filename, 'w') as fp:
        json.dump(numbers, fp)

if __name__ == '__main__':
    main()
    sys.exit(1)