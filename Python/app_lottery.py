"""A class that can be used to represent lottery """

import sys

from random import choice

class Lottery:
    def __init__(self):
        self.alphanum = [i for i in range(0, 10)]
        self.alphanum += ['A', 'B', 'C', 'D', 'E']

    def show_lottery(self):
        ticket = f"{choice(self.alphanum)}{choice(self.alphanum)}{choice(self.alphanum)}{choice(self.alphanum)}"
            
        print(f"\nAny ticket matches these four numbers or letters \"{ticket}\" wins a prize.")

def main():
    lot = Lottery()
    lot.show_lottery()

if __name__ == '__main__':
    main()
    sys.exit(1)
