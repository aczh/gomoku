from .. threat.threat_search import get_fives, get_fours, get_threes, get_threats
from .. threat.threat import Three
from .. utils import to_row, ThreatType
from .. board import Board
import random

VERBOSE=1

class ThreatSpace:
    def __init__(self):
        self.execs = 0

    def make_move(self, b):
        print("-----------------------------------------------------------------------------------------")
        b.print()

        self.execs = 0
        moves = self.search(b)
        print(f'executed {self.execs} times')
        if moves:
            if VERBOSE: print(f'Winning line being played: {[to_row(move) for move in moves]}')
            return moves[0]

        self.execs = 0
        moves = self.search(b, current=False)
        print(f'executed {self.execs} times')
        if moves:
            if VERBOSE: print(f'Winning line being blocked: {[to_row(move) for move in moves]}')
            return moves[0]


        print('Random move...')
        return random.choice(self.valid_moves(b))

    def search(self, b, seen=set(), moves=[], current=True):
        self.execs += 1
        new_threats = set(get_threats(b, current=current))
        diff = new_threats.difference(seen)
        seen = new_threats.union(seen)

        for t in diff:
            if t.type == ThreatType.FIVE or t.type == ThreatType.STRAIGHT_FOUR: return [*moves, t.gain_square]

            _b = Board(b1=b.b1, b2=b.b2, turns=b.turns)
            _b.force_index(t.gain_square, current=current)
            for cost in t.cost_squares:
                _b.force_index(cost, current=not current)

            ans = self.search(_b, seen, moves=[*moves, t.gain_square], current=current)
            if ans: return ans

    def valid_moves(self, b):
        moves = [
            (r, c)
            for r in range(b.size) for c in range(b.size)
            if b.is_valid_move(r, c)
        ]
        return moves
