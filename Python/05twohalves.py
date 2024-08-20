
import sys

def main():
    s = input()
    l = len(s)
    l = int((l+1) / 2)

    ns = s[l:] + s[0:l]
    print(ns)

if __name__ == '__main__':
    main()
    sys.exit(0)

