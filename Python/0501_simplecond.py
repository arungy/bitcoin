#!/usr/bin/python

import sys

def main():
    car = 'suburu'
    print("Is car == 'suburu'? I predict True.")
    print(car == 'suburu')
    
    print("Is car == 'audi'? I predict False.")
    print(car == 'audi')
    
    #2nd set
    print()
    fav_os = 'linux'
    print("Is fav_os == 'linux'? I predict True.")
    print(fav_os == 'linux')
    
    print("Is fav_os == 'windows'? I predict False.")
    print(fav_os == 'windows')
    
    print()
    fav_editor = 'notepad++'
    print("Is fav_editor == 'notepad++'? I predict True.")
    print(fav_editor == 'notepad++')
    
    print("Is fav_editor == 'sublime'? I predict False.")
    print(fav_editor == 'sublime')

if __name__ == '__main__':
    main()
    sys.exit(0)