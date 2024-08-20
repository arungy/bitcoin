"""A file read the the pi value"""

import sys

def main():
    filename = './pi_million_digits.txt'
    
    with open(filename) as f:
        lines = f.readlines()
    
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
        
    birthday = input("Enter your birthday, in the form mmddyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appears in the first million digits of pi!")
    
if __name__ == '__main__':
    main()
    sys.exit(1)
