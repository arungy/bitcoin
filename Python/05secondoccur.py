
import sys

def main():
    s = input()

    p = s.find('f')
    if p == -1:
        print(-2)
    else:
        p = s.find('f', p+1)
        if p == -1:
            print(-1)
        else:
            print(p)

if __name__ == '__main__':
    main()
    sys.exit(0)
