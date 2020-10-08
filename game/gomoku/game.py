'''
Class that plays a game of Gomoku.
'''

from . board import Board
from . threat.threat_search import has_five
from . utils import to_row

VERBOSE=1

class Game:
    def __init__(self, p1, p2, on_p1_move=None, on_p2_move=None):
        self.p1 = p1
        self.p2 = p2
        self.b = Board()
        self.history = []
        self.on_p1_move = on_p1_move
        self.on_p2_move = on_p2_move

    def play(self):
        if VERBOSE:
            print('\n====================================================================')
            print('Player {}\'s turn to move.'.format(self.b.turns % 2 + 1))
            print(self.b)

        if self.b.turns % 2 == 0:
            self.p1.request_move(self.b, self)
        else:
            self.p2.request_move(self.b, self)

    def make_move(self, move):
        if isinstance(move, int):
            move = to_row(move)
        self.b.move(*move)
        self.history.append(move)

        if VERBOSE:
            print('\n====================================================================')
            print(f'Player {2 - self.b.turns % 2} placed their piece at {move[0]}, {move[1]}')
            print(f'Player {self.b.turns % 2 + 1}\'s turn to move.')
            print(self.b)

        if has_five(self.b) or has_five(self.b, current=False):
            self.on_win()
        elif self.b.turns == self.b.size * self.b.size:
            self.on_draw()
        else:
            self.play()

    def on_win(self):
        print('We have a winner!')
        print(self.b)

    def on_draw(self):
        print('Drawn game!')
        print(self.b)
