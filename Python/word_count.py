"""Count the approximate number of words in a file"""

import sys

def count_words(filename):
    try:
        with open(filename) as fp:
            contents = fp.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not available.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def main():
    filenames =['programming.txt', 'division_calculator.py',  'pi_string.py', 'edison.txt']
    
    for filename in filenames:
        count_words(filename)

if __name__ == '__main__':
    main()
    sys.exit(1)

