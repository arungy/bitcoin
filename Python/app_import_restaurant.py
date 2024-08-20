"""A class that can represent import restaurant"""

import sys

from restaurant import Restaurant

def main():
    ch_restaurant = Restaurant('Sawarama', 'non vegeterian')
    ch_restaurant.describe_restaurant()

if __name__ == '__main__':
    main()
    sys.exit(1)
