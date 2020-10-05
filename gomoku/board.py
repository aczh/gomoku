import sys
import gmpy2
from . import utils

class Board:
    def __init__(self, size=15, b1=0, b2=0, turns=0):
        self.size = size
        self.turns = turns

        self.mask = 53919893334301279589334030174039261347274288845081144962207220498431

        self.b1 = b1
        self.b2 = b2
        self.o = self.b1 | self.b2
        self.e = self.o ^ self.mask

    def copy(self):
        return Board(size=self.size, b1=self.b1, b2=self.b2, turns=self.turns)

    def moves(self, moves=[], p1=[], p2=[]):
        tmp = self.turns
        self.turns = 0
        for move in p1:
            if not isinstance(move, int):
                move = move[0] * self.size + move[1]
            self.force_index(move)

        for move in p2:
            if not isinstance(move, int):
                move = move[0] * self.size + move[1]
            self.force_index(move, current=False)
        self.turns = tmp + len(p1) + len(p2)

    def get_board(self, current=True):
        '''
        Returns board of current player if current is set to True.
        '''
        if self.turns % 2 == 0 ^ current:
            return self.b2
        return self.b1

    #####################
    # FORCE MOVE
    #####################
    def force_index(self, index, current=True):
        if self.turns % 2 == 0 ^ current:
            self.b2 = gmpy2.bit_set(self.b2, index)
        else:
            self.b1 = gmpy2.bit_set(self.b1, index)

        self.o = gmpy2.bit_set(self.o, index)
        self.e = gmpy2.bit_clear(self.e, index)

    def force_move(self, r, c, current=True):
        self.force_index(r * self.size + c, current=current)

    def force_undo_index(self, index, current=True):
        if self.turns % 2 == 0 ^ current:
            self.b2 = gmpy2.bit_clear(self.b2, index)
        else:
            self.b1 = gmpy2.bit_clear(self.b1, index)

        self.e = gmpy2.bit_set(self.e, index)
        self.o = gmpy2.bit_clear(self.o, index)

    #####################
    # MOVE
    #####################
    def is_valid_index(self, index):
        return 0 <= index < self.size * self.size and not gmpy2.bit_test(self.e, index)

    def is_valid_move(self, r, c):
        return c >= 0 and r >= 0 and r < self.size and c < self.size and gmpy2.bit_test(self.e, r * self.size + c)

    def move_index(self, index):
        if not self.is_valid_index(index): raise Exception(f'Invalid cell: {index // 15}, {index % 15}')
        self.force_index(index)
        self.turns += 1

    def move(self, r, c):
        self.move_index(r * 15 + c)

    #####################
    # VALID
    #####################
    def is_valid_index(self, index):
        return 0 <= index < self.size * self.size and gmpy2.bit_test(self.e, index)

    def is_valid_move(self, r, c):
        return c >= 0 and r >= 0 and r < self.size and c < self.size and gmpy2.bit_test(self.e, r * self.size + c)

    def __repr__(self):
        return f'b1={self.b1}, b2={self.b2}, turns={self.turns}'

    def __str__(self):
        s = []
        s.append('===================================')
        s.append('    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 ')
        s.append('    ______________________________')
        for row in range(self.size):
            r = f'{row:>2} |'
            for col in range(self.size):
                bit_index = row * 15 + col
                if gmpy2.bit_test(self.b1, bit_index): r += 'o '
                elif gmpy2.bit_test(self.b2, bit_index): r += 'x '
                else: r += '- '
            s.append(r)
        s.append(f'b1={self.b1}, b2={self.b2}, turns={self.turns}')
        s.append('===================================')
        return '\n'.join(s)

    def __eq__(self, other):
        return self.b1 == other.b1 and self.b2 == other.b2

    def __hash__(self):
        return hash((self.b1, self.b2))
