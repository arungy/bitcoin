
import sys

def main():
    #s = 'Abrakadabra'
    s = input()
    print(s[2])
    print(s[-2:-1])
    print(s[0:5])
    print(s[0:-2])

    for i in range(0, len(s), 2):
        print(i, s[i])
    print()

    for i in range(1, len(s), 2):
        print(i, s[i])
    print()

    print(s[::-1])
    print()

    for i in range(len(s)-1, -1, -2):
        print(i, s[i])
    print()

    print(len(s))


if __name__ == '__main__':
    main()
    sys.exit(0)

