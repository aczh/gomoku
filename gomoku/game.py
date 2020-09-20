from . import board
from . threat.threat_search import has_five

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.b = board.Board()

    def on_win(self):
        print('We have a winner!')

    def on_draw(self):
        print('Drawn game!')

    def play(self):
        while not has_five(self.b) and not has_five(self.b, current=False):
            self.b.print()

            if self.b.turns == self.b.size * self.b.size:
                self.on_draw(self)
                break

            if self.b.turns % 2 == 0:
                move = self.p1.make_move(self.b)
            else:
                move = self.p2.make_move(self.b)

            self.b.move(*move)

        self.on_win()
