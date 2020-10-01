import sys
import gmpy2
from . import utils

class Board:
    def __init__(self, size=15, b1=0, b2=0, turns=0):
        self.size = size
        # board of player 1
        self.b1 = b1
        # board of player 2
        self.b2 = b2

        self.turns = turns

    def moves(self, moves=[], p1=[], p2=[]):
        for move in p1:
            if not isinstance(move, int):
                move = move[0] * self.size + move[1]
            self.b1 = gmpy2.bit_flip(self.b1, move)
            self.turns += 1

        for move in p2:
            if not isinstance(move, int):
                move = move[0] * self.size + move[1]
            self.b2 = gmpy2.bit_flip(self.b2, move)
            self.turns += 1

    def get_board(self, current=True):
        '''
        Returns board of current player if current is set to True.
        '''
        if self.turns % 2 == 0:
            return self.b1 if current else self.b2
        return self.b2 if current else self.b1

    #####################
    # FORCE MOVE
    #####################
    def force_index(self, index, current=True):
        if self.turns % 2 == 0:
            if current:
                self.b1 = gmpy2.bit_flip(self.b1, index)
            else:
                self.b2 = gmpy2.bit_flip(self.b2, index)
        else:
            if current:
                self.b2 = gmpy2.bit_flip(self.b2, index)
            else:
                self.b1 = gmpy2.bit_flip(self.b1, index)

    def force_move(self, r, c, current=True):
        self.force_index(r * self.size + c, current=True)

    #####################
    # MOVE
    #####################
    def is_valid_index(self, index):
        return self.is_valid_move(index // self.size, index % self.size)

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

    def print(self):
        '''Pretty prints the board.'''
        print('     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 ')
        print('     ______________________________')
        for row in range(self.size):
            print('{:>2}  |'.format(row), end='')
            for col in range(self.size):
                bit_index = row * 15 + col
                if gmpy2.bit_test(self.b1, bit_index):
                    print('o ', end='')
                elif gmpy2.bit_test(self.b2, bit_index):
                    print('x ', end='')
                else:
                    print('- ', end='')
            print('')
        print('==================================')
        print(f'b1={self.b1}, b2={self.b2}, turns={self.turns}')
