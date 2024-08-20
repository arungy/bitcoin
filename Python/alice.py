
import sys

def main():
    filename = 'alice.txt'

    try:
        with open(filename, encoding='utf-8') as fp:
            contents = fp.read()
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

if __name__ == '__main__':
    main()
    sys.exit(1)
