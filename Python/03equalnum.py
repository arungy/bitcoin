
import sys

def main():
    print('Enter three values x, y & z:')

    x = int(input())
    y = int(input())
    z = int(input())

    if x == y and x == z:
        print('3 values are equal')
    elif x == y or y == z:
        print('2 values are equal')
    else:
        print('Zero values are equal')

if __name__ == '__main__':
    main()
    sys.exit(0)

