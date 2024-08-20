
import sys

def main():
    s = input()
    p = s.find(' ')
    ns = s[p+1:] + s[0:p]

    print(ns)

if __name__ == '__main__':
    main()
    sys.exit(0)


