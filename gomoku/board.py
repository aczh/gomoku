import sys
import gmpy2

class Board:
    def __init__(self, size=15):
        self.size = size
        # board of player 1
        self.b1 = 0
        # board of player 2
        self.b2 = 0
        # occupied squares
        self.o = 0
        self.turns = 0
        self.history = []

    def moves(self, moves=[], p1=[], p2=[]):
        if p1 and p2 and len(p1) == len(p2):
            moves = [val for pair in zip(p1, p2) for val in pair]
        for m in moves:
            self.move(*m)

    def is_valid_index(self, index):
        return self.is_valid_move(index // self.size, index % self.size)

    def is_valid_move(self, r, c):
        '''
        Returns True if r, c fall within size constraints and the space is unoccupied.
        '''
        return c >= 0 and r >= 0 and r < self.size and c < self.size and not gmpy2.bit_test(self.o, r * self.size + c)

    def get_board(self, current=True):
        '''
        Returns board of current player if current is set to True.
        '''
        if self.turns % 2 == 0:
            return self.b1 if current else self.b2
        return self.b2 if current else self.b1

    def move(self, r, c):
        '''
        Make move.
        Increment turn count.
        Update move history.
        '''
        self.history.append((self.b1, self.b2))

        if not self.is_valid_move(r, c):
            raise Exception(f'Invalid move: {r}, {c}')

        # update player boards
        if self.turns % 2 == 0:
            self.b1 = gmpy2.bit_flip(self.b1, r * self.size + c)
        else:
            self.b2 = gmpy2.bit_flip(self.b2, r * self.size + c)

        # update occupied spaces
        self.o = self.b1 | self.b2

        # update turns and moves
        self.turns += 1

    def print(self):
        '''Pretty prints the board.'''
        print('=============================')
        for r in range(self.size):
            row = []
            for c in range(self.size):
                bit_index = r * self.size + c
                if gmpy2.bit_test(self.b1, bit_index):
                    row.append('o')
                elif gmpy2.bit_test(self.b2, bit_index):
                    row.append('x')
                else:
                    row.append('-')
            print(' '.join(row))
