#!/usr/bin/python

import sys

def main():
    players = ['charles', 'martina', 'micheal' , 'florence', 'eli']
    print(players[0:3])
    print(players[1:4])
    print(players[:4])
    print(players[2:])
    print(players[-2:])
    
    print("\nHere are the first three players on my team:")
    for player in players[:3]:
        print(player.title())

if __name__ == '__main__':
    main()
    sys.exit(0)