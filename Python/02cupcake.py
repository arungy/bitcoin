
import sys

def main():
    print('cup cake')

    A = int(input())
    B = int(input())
    N = int(input())

    cost = (A * 100 * N) + (B * N)
    print('total cost:', (cost // 100), 'Rupee', (cost % 100), 'paise')


if __name__ == '__main__':
    main()
    sys.exit(0)
