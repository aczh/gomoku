'''
Class that plays a game of Gomoku.
'''

from . board import Board
from . threat.threat_search import has_five
from . utils import to_row

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.b = Board()

    def on_win(self):
        print('We have a winner!')
        print(self.b)

    def on_draw(self):
        print('Drawn game!')
        print(self.b)

    def play(self, verbose=1):
        print('\n====================================================================')
        print('Player {}\'s turn to move.'.format(self.b.turns % 2 + 1))
        print(self.b)

        while not has_five(self.b) and not has_five(self.b, current=False):
            if self.b.turns == self.b.size * self.b.size:
                self.on_draw()
                break

            if self.b.turns % 2 == 0:
                move = self.p1.make_move(self.b)
            else:
                move = self.p2.make_move(self.b)

            if isinstance(move, int):
                move = to_row(move)

            self.b.move(*move)
            if verbose:
                print('\n====================================================================')
                print(f'Player {self.b.turns % 2} placed their piece at {move[0]}, {move[1]}')
                print(f'Player {self.b.turns % 2 + 1}\'s turn to move.')
                print(self.b)

        self.on_win()
