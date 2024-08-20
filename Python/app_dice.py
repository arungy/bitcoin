"""An class that can be used to represent dice"""

import sys
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print("\n")
        for i in range(0, 10):
            print(f"On {self.sides} face die, your side is {randint(1, self.sides)}!")

def main():
    die = Die()
    die.roll_die()
        
    die20 = Die(20)
    die20.roll_die()
        
if __name__ == '__main__':
    main()
    sys.exit(1)
    