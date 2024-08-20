
import sys

def main():
    print('Enter the x & y value:')
    a = int(input())
    b = int(input())

    if a > b:
        print(a, 'is bigger than', b)
    else:
        print(a, 'is lesser than', b)

if __name__ == '__main__':
    main()
    sys.exit(0)

