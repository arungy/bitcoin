#!/usr/bin/python

import sys

def main():
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]

    my_foods.append('cannoli')
    friend_foods.append('ice cream')

    print("My favourite foods are: ")
    for food_item in my_foods:
        print(food_item.title())

    print("\nMy friend's favourite foods are: ")
    for food_item in friend_foods:
        print(food_item.title())

if __name__ == '__main__':
    main()
    sys.exit(0)