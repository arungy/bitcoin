
import sys

def main():
    s = input()
    l = len(s)

    ns = ''
    n = 0
    for i in range(0, l):
        if i % 3 != 0:
            ns = ns + s[i]

    print(ns)

if __name__ == '__main__':
    main()
    sys.exit(0)


