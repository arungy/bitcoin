#!/usr/bin/python

import sys

def main():
    print('Enter the number of records:', end=' ')
    N = int(input())

    electCand = dict()

    for i in range(0, N):
        line = str(input()).split()

        name = str(line[0])
        vote = int(line[1])

        if name in electCand:
            electCand[name] = electCand[name] + vote
        else:
            electCand[name] = vote

    print()
    for name, vote in sorted(electCand.items()):
        print(name + " : " + str(vote))


if __name__ == '__main__':
    main()
    sys.exit(0)

