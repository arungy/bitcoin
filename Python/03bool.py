
import sys

def main():
    print('Bool example:')

    print(2<5)
    print(2>5)
    print()

    #bool
    print(bool(-10))
    print(bool(0))
    print(bool(10))
    print()

    print(bool(''))
    print(bool('abc'))

    print('\nEnter the x & y value"')

    x = int(input())
    y = int(input())

    if x % 10 == 0 or y % 10 == 0:
        print('YES')
    else:
        print('NO')

    if x > 0 and y > 0:
        print('Quadrant I')
    elif x > 0 and y < 0:
        print('Quadrant IV')
    elif y > 0:
        print('Quadrant II')
    else:
        print('Quadrant III')
    

if __name__ == '__main__':
    main()
    sys.exit(0)
