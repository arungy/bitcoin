
import sys

def main():
    s = input()

    f = s.find('h')
    l = s.rfind('h')
   
    ns = s[0:f+1] + s[f+1:l].replace('h', 'H') + s[l:]
    print(ns)

if __name__ == '__main__':
    main()
    sys.exit(0)


