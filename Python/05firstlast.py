
import sys

def main():
    s = input()

    f = s.find('f')
    l = s.rfind('f')

    if f == l and f != -1 and l != -1:
        print("fist & last occurance:", f)
    elif f != l:
        print("fist occurance:", f)
        print("last occurance:", l)
    else:
        print()

if __name__ == '__main__':
    main()
    sys.exit(0)

