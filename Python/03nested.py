
import sys

def main():
    print('Enter the x & y value:')

    x = int(input())
    y = int(input())

    if x > 0:
        if y > 0:
            print('Quadrant I')
        else:
            print('Quadrant IV')
    else:
        if y > 0:
            print('Quadrant II')
        else:
            print('Quadrant III')

if __name__ == '__main__':
    main()
    sys.exit(0)
