#!/usr/bin/python

import sys
import math

def main():
    print("Enter the number of elements:", end=' ')
    N = int(input())

    englat_text = [str(input()) for i in range(0, N)]

    englat_dict = dict()
    for wd in englat_text:
        wdelm = wd.replace(' ', '').replace('-', ' ').replace(',', ' ').split()
        englat_dict[wdelm[0]] = wdelm[1:]

    lateng_dict = dict()
    for key, val in englat_dict.items():
        for v in val:
            if v in lateng_dict:
                lateng_dict[v] += ", " + str(key)
            else:
                lateng_dict[v] = str(key)
   
    lateng_text = []
    for key, val in sorted(lateng_dict.items()):
        lateng_text.append(key + " - " + val)

    print("\n%d" % (len(lateng_text)))
    for e in lateng_text:
        print(e)


if __name__ == '__main__':
    main()
    sys.exit(0)

