#!/usr/bin/python

import sys

def main():
    #1st
    car = 'duster'
    print("car = ", car)
    print("car == 'duster':", (car == 'duster'))
    print("car == 'ecosports':", (car == 'ecosports'))

    car = 'ecosports'
    print("\ncar = ", car)
    print("car != 'duster':", (car != 'duster'))
    print("car != 'ecosports':", (car != 'ecosports'))

    #2nd
    watch = 'Rolex'
    print("\nwatch = ", watch)
    print("watch == 'rolex':", (watch == 'rolex'))
    print("watch.lower() == 'rolex':", (watch.lower() == 'rolex'))

    #3rd
    retirement_age = 58
    print("\nretirement_age = ", retirement_age)
    print("retirement_age == 58 :", (retirement_age == 58))
    print("retirement_age != 58 :", (retirement_age != 58))
    print("retirement_age >  58 :", (retirement_age >  58))
    print("retirement_age >= 58 :", (retirement_age >= 58))
    print("retirement_age <  58 :", (retirement_age <  58))
    print("retirement_age <= 58 :", (retirement_age <= 58))

    #4th
    boy_age = 17
    girl_age = 18

    print("\nboy_age:", boy_age, "girl_age:", girl_age)
    if (boy_age >= 18) and (girl_age >= 18):
        print("Boy and Girl are major as per Govt age regulation.")
    else:
        print("Either Boy or Girl is not major as per Govt age regulation.")

    #5th
    computer_pars = ['monitor', 'key board', 'cpu', 'power cables']

    print("\nIs 'key board' available in computer_parts? I predict True.")
    print('key board' in computer_pars)

    print("\nIs 'wireless mouse' not available in computer_parts? I predict True.")
    print('wireless mouse' not in computer_pars)

if __name__ == '__main__':
    main()
    sys.exit(0)