
import sys

def main():
    s = input()

    f = s.find('h')
    l = s.rfind('h')

    if f != -1 and l != -1:
        ns = s.replace(s[f:l+1],'')
        print(ns)

if __name__ == '__main__':
    main()
    sys.exit(1)


