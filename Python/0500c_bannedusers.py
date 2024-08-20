#!/usr/bin/python

import sys

def main():
    banned_users = ['andrew', 'carolina', 'david']
    user = 'marie'
    
    if user not in banned_users:
        print(user.title() + ", you can post a response if you wish.")

if __name__ == '__main__':
    main()
    sys.exit(0)