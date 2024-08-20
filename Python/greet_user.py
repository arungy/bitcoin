"""Greet user"""

import sys
import json

def main():
    filename = 'username.json'

    with open(filename) as fp:
        username = json.load(fp)
        print(f"Welcome back, {username}")

if __name__ == '__main__':
    main()
    sys.exit(1)
