import sys
import gmpy2
from . import utils

class Board:
    def __init__(self, size=15, b1=0, b2=0, turns=0):
        self.size = size

        self.b1 = b1
        self.b2 = b2

        self.b1_h = 0
        self.b2_h = 0

        # main diagonal
        self.b1_d1_a = 0
        self.b1_d1_b = 0

        self.b2_d1_a = 0
        self.b2_d1_b = 0

        # off diagonal
        self.b1_d2_a = 0
        self.b1_d2_b = 0

        self.b2_d2_a = 0
        self.b2_d2_b = 0


        self.turns = 0
        for i in range(225):
            if gmpy2.bit_test(self.b1, i):
                self.force_index(i)
            if gmpy2.bit_test(self.b2, i):
                self.force_index(i, current=False)

        self.turns = turns

    def gb(self, current=True, inc=1):
        if self.turns % 2 == 0 and current:
            if inc == 1:
                return [self.b1_h]
            if inc == self.size:
                return [self.b1]
            if inc == self.size + 1:
                return [self.b1_d1_a, self.b1_d1_b]
            if inc == self.size - 1:
                return [self.b1_d2_a, self.b1_d2_b]
        else:
            if inc == 1:
                return [self.b2_h]
            if inc == self.size:
                return [self.b2]
            if inc == self.size + 1:
                return [self.b2_d1_a, self.b2_d1_b]
            if inc == self.size - 1:
                return [self.b2_d2_a, self.b2_d2_b]


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

    def get_board(self, current=True, inc=1):
        '''
        Returns board of current player if current is set to True.
        '''
        if self.turns % 2 == 0 and current:
            return self.b1
        return self.b2

    def get_boards(self, current=True):
        if self.turns % 2 == 0 and current:
            return [self.b1_h, self.b1, self.b1_d1_a, self.b1_d1_b, self.b1_d2_a, self.b1_d2_b]
        return [self.b2_h, self.b2, self.b2_d1_a, self.b2_d1_b, self.b2_d2_a, self.b2_d2_b]


    #####################
    # FORCE MOVE
    #####################
    def force_index(self, index, current=True):
        r = index // self.size
        c = index % self.size

        index_h = r + c * self.size
        index_d1 = r * self.size + (c - r)
        index_d2 = r * self.size + (c + r) % 15

        if self.turns % 2 == 0 and current:
            self.b1 = gmpy2.bit_set(self.b1, index)
            self.b1_h = gmpy2.bit_set(self.b1_h, index_h)

            if 14 - r >= c:
                self.b1_d2_a = gmpy2.bit_set(self.b1_d2_a, index_d2)
            else:
                self.b1_d2_b = gmpy2.bit_set(self.b1_d2_b, index_d2)

            if r <= c:
                self.b1_d1_a = gmpy2.bit_set(self.b1_d1_a, index_d1)
            else:
                self.b1_d1_b = gmpy2.bit_set(self.b1_d1_b, index_d1)


        else:
            self.b2 = gmpy2.bit_set(self.b2, index)
            self.b2_h = gmpy2.bit_set(self.b2_h, index_h)

            if 14 - r >= c:
                self.b2_d2_a = gmpy2.bit_set(self.b2_d2_a, index_d2)
            else:
                self.b2_d2_b = gmpy2.bit_set(self.b2_d2_b, index_d2)

            if r <= c:
                self.b2_d1_a = gmpy2.bit_set(self.b2_d1_a, index_d1)
            else:
                self.b2_d1_b = gmpy2.bit_set(self.b2_d1_b, index_d1)


    def force_move(self, r, c, current=True):
        self.force_index(r * self.size + c, current=True)

    #####################
    # MOVE
    #####################
    def is_valid_index(self, index):
        return 0 <= index < self.size * self.size and not gmpy2.bit_test(self.b1 | self.b2, index)

    def is_valid_move(self, r, c):
        '''
        Returns True if r, c fall within size constraints and the space is unoccupied.
        '''
        return c >= 0 and r >= 0 and r < self.size and c < self.size and not gmpy2.bit_test(self.b1 | self.b2, r * self.size + c)

    def move_index(self, index):
        if not self.is_valid_index(index): raise Exception(f'Invalid index: {index}')

        # update player boards
        self.force_index(index)

        # update turns and moves
        self.turns += 1

    def move(self, r, c):
        self.move_index(r * 15 + c)

    #####################
    # VALID
    #####################
    def is_valid_index(self, index):
        return self.is_valid_move(index // self.size, index % self.size)

    def is_valid_move(self, r, c):
        '''
        Returns True if r, c fall within size constraints and the space is unoccupied.
        '''
        return c >= 0 and r >= 0 and r < self.size and c < self.size and not gmpy2.bit_test(self.b1 | self.b2, r * self.size + c)

    def __str__(self):
        s = []
        s.append('===================================')
        # s.append('    a b c d e f g h i j k l m n o ')
        s.append('    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 ')
        s.append('    ______________________________')
        for row in range(self.size):
            # r = f'{15-row:>2} |'
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
