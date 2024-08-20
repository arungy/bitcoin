#!/usr/bin/ev python3

import sys

def main():
    print('digi clock')

    min = int(input())
    hr = min // 60
    mt = min % 60

    print('digital time is', hr, ':', mt)


if __name__ == '__main__':
    main()
    sys.exit()

