
import sys

def main():
    print('if example\n')
    x = int(input())

    #if x > 0:
    #    print(x)
    #else:
    #    print(-x)

    if x < 0:
        x = -x
    print(x)

    k = int(input())
    print(abs(k))

if __name__ == '__main__':
    main()
    sys.exit(0)

