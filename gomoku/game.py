from . import board
from . threat.threat_search import has_five
from . utils import to_row

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.b = board.Board()

    def on_win(self):
        print('We have a winner!')
        self.b.print()

    def on_draw(self):
        print('Drawn game!')

    def play(self, verbose=1):
        while not has_five(self.b) and not has_five(self.b, current=False):

            print('\n\n-------------------------------------------')
            print('Player {}\'s turn to move.'.format(self.b.turns % 2 + 1))
            self.b.print()

            if self.b.turns == self.b.size * self.b.size:
                self.on_draw(self)
                break

            if self.b.turns % 2 == 0:
                move = self.p1.make_move(self.b)
            else:
                move = self.p2.make_move(self.b)

            if isinstance(move, int):
                move = to_row(move)

            if verbose:
                print('\n\n====================================================================')
                print('Player {} placed their piece at: {}, {}'.format(self.b.turns % 2 + 1, *move))
                print('====================================================================')

            self.b.move(*move)

        self.on_win()
