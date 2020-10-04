from .. threat.threat_search import get_fives, get_fours, get_threes, get_threats, has_five
from .. threat.threat_space import threat_space_search
from .. threat.threat import Three
from .. utils import to_row, ThreatType
from .. board import Board
import random
import time

VERBOSE=1

class ThreatSpace:
    def __init__(self):
        self.winning_line = []

    def touching(self, b, index):
        t = 0
        dirs = [-1, 1, -b.size, b.size, -b.size + 1, b.size - 1, -b.size - 1, b.size + 1]
        for d in dirs:
            if 0 <= index + d < 225 and not b.is_valid_index(index + d):
                t += 1
        return t

    def score_moves(self, b):
        scored_moves = []
        for move in self.valid_moves(b):
            _b = b.copy()
            _b.force_index(move)
            score = len(get_threes(_b)) * 5 - len(get_threes(_b, current=False))
            scored_moves.append((score, move))
        scored_moves.sort(reverse=True)
        return scored_moves

    def forced_moves(self, b):
        # make 5
        forced = get_fives(b)
        if forced: return forced[0].gain_square

        # block 5
        forced = get_fives(b, current=False)
        if forced: return forced[0].gain_square

        # make straight 4
        forced = [t for t in get_fours(b) if t.type == ThreatType.STRAIGHT_FOUR]
        if forced: return forced[0].gain_square

        return None

    def valid_moves(self, b):
        return [i for i in range(225) if b.is_valid_index(i)]

    def make_move(self, b):
        if b.turns == 0: return (7, 7)

        forced = self.forced_moves(b)
        if forced:
            print(f'Making forced move...: {to_row(forced)}')
            self.winning_line = []
            return forced

        if self.winning_line:
            if VERBOSE: print(f'Saved winning line being played: {[to_row(move) for move in self.winning_line[::-1]]}')
            return self.winning_line.pop()

        # search for winning line
        moves = threat_space_search(b)
        if moves:
            if VERBOSE: print(f'Winning line being played: {[to_row(move) for move in moves]}')
            self.winning_line = moves[::-1]
            return self.winning_line.pop()

        # search for winning line in opponent's board
        moves = threat_space_search(b, current=False)
        if moves:
            if VERBOSE: print(f'Winning line being blocked: {[to_row(move) for move in moves]}')
            return moves[0]

        # make a move based on simple heuristic
        score_moves = self.score_moves(b)
        best_moves = [tup[1] for tup in score_moves][:10]
        # best_moves = [tup[1] for tup in score_moves if tup[0] == score_moves[0][0]][:10]
        for move in best_moves:
            _b = b.copy()
            _b.force_index(move)
            moves = [t for t in threat_space_search(_b)]
            if moves:
                moves.insert(0, move)
                if VERBOSE: print(f'Threatening line being played: {[to_row(move) for move in moves]}')
                return moves[0]

        print('Random move...')
        return random.choice([tup[1] for tup in score_moves if tup[0] == score_moves[0][0]][:10])
