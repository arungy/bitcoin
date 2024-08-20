
import sys

def main():
    print('Enter the value for x, y & z:')
    v0 = int(input())
    v1 = int(input())
    v2 = int(input())

    print('\nThe smallest number is:')

    if v0 < v1 and v0 < v2:
        print(v0)
    elif v1 < v2:
        print(v1)
    else:
        print(v2)

if __name__ == '__main__':
    main()
    sys.exit(0)

