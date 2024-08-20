#!/usr/bin/python

import sys

def main():
    buffet_foods = ('polavo', 'veg briyani', 'fried fish', 'chicken loolipop', 'mutton curry')
    print("Buffet Menu:")
    for food in buffet_foods:
        print(food.title())

    #buffet_foods[1] = 'chicken briyani'

    print()
    buffet_foods = ('dal kichadi', 'chicken briyani', 'fried fish', 'chicken loolipop', 'mutton curry')
    print("New Buffet Menu:")
    for food in buffet_foods:
        print(food.title())

if __name__ == '__main__':
    main()
    sys.exit(0)
