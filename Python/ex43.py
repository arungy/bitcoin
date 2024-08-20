from ex43a import *

class Game(object):
    def __init__(self, start):
        self.start = start
        self.list = {   #list 'function name' -> class name
            'death'               : DeathRoom,
            'princess_lives_here' : PrinceRoom,
            'gold_koi_pond'       : GoldRoom,
            'bear_with_sword'     : BearRoom,
            'big_iron_gate'       : IronRoom
        }

    def play(self):
        next = self.start

        while True:
            print "\n--------"

            clsobj = self.list[next]()  #create object of that class
            room = getattr(clsobj, next)
            next = room()

a_game = Game('princess_lives_here')
a_game.play()