def bit_flip(n, i):
    '''Flips bit at index i.'''
    return (n ^ (1 << (i - 1)))

def bit_get(n, i):
    '''Gets bit at index i.'''
    return 1 if n & (1 << (i - 1)) else 0

class Board:
    def __init__(self, size=15):
        self.size = size
        self.b1 = 0
        self.b2 = 0
        self.turns = 0
        self.moves = []

    def print(self):
        for r in range(1, self.size + 1):
            row = []
            for c in range(1, self.size + 1):
                bit_index = r * self.size + c
                if bit_get(self.b1, bit_index):
                    row.append('x')
                elif bit_get(self.b2, bit_index):
                    row.append('o')
                else:
                    row.append('-')
            print(' '.join(row))

    def is_valid_move(self, r, c):
        move_bit = r * 15 + c
        return r <= 15 and c <= 15 and not (bit_get(self.b1, move_bit) or bit_get(self.b2, move_bit))

    def move(self, r, c):
        if not self.is_valid_move(r, c):
            return False

        if self.turns % 2 == 0:
            self.b1 = bit_flip(self.b1, r * self.size + c)
        else:
            self.b2 = bit_flip(self.b2, r * self.size + c)
        self.turns += 1
        self.moves.append((r, c))
        return True

    def check_win(self, b):
        h = b & (b >> 1) & (b >> 2) & (b >> 3) & (b >> 4)
        v = b & (b >> self.size) & (b >> self.size * 2) & (b >> self.size * 3) & (b >> self.size * 4)
        d1 = b & (b >> (self.size + 1)) & (b >> (self.size * 2 + 2)) & (b >> (self.size * 3 + 3)) & (b >> (self.size * 4 + 4))
        d2 = b & (b >> (self.size - 1)) & (b >> (self.size * 2 - 2)) & (b >> (self.size * 3 - 3)) & (b >> (self.size * 4 - 4))
        print(bin(h))
        print(bin(v))

b = Board()
print(b.move(1, 1))
print(b.move(2, 1))
print(b.move(1, 2))
print(b.move(3, 1))
print(b.move(1, 3))
print(b.move(4, 1))
print(b.move(1, 4))
print(b.move(5, 1))
print(b.move(1, 5))
print(b.move(6, 1))
b.winning_move(b.b1)
# print(bin(b.b2))
b.winning_move(b.b2)
b.print()
