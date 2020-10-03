from .. threat.threat_search import get_fives, get_fours, get_threes, get_threats, has_five
from .. threat.threat import Three
from .. utils import to_row, ThreatType
from .. board import Board
import random
import time

VERBOSE=1

class ThreatSpace:
    def __init__(self):
        self.winning_line = []
        self.nodes = 0
        self.execs = 0
        self.i = 0
        self.seen = set()

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
            score = len(get_threes(_b))
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
            if VERBOSE: print(f'Saved winning line being played: {[to_row(move.gain_square) for move in self.winning_line[::-1]]}')
            return self.winning_line.pop().gain_square

        # search for winning line
        moves = self.search(b)
        if moves:
            if VERBOSE: print(f'Winning line being played: {[to_row(move.gain_square) for move in moves]}')
            self.winning_line = moves[::-1]
            return self.winning_line.pop().gain_square

        # search for winning line in opponent's board
        moves = self.search(b, current=False)
        if moves:
            if VERBOSE: print(f'Winning line being blocked: {[to_row(move.gain_square) for move in moves]}')
            return moves[0].gain_square

        # make a move based on simple heuristic
        score_moves = self.score_moves(b)
        best_moves = [tup[1] for tup in score_moves if tup[0] == score_moves[0][0]][:10]
        for move in best_moves:
            _b = b.copy()
            _b.force_index(move)
            moves = [t.gain_square for t in self.search(_b)]
            if moves:
                moves.insert(0, move)
                if VERBOSE: print(f'Threatening line being played: {[to_row(move) for move in moves]}')
                return moves[0]

        print('Random move...')
        return random.choice(best_moves)

    def confirm_winning_line(self, b, threats):
        if len(threats) == 0: return True
        self.i += 1

        if get_fives(b): return True
        if get_fives(b, current=False): return False

        t = threats[0]
        b.move_index(t.gain_square)

        if not get_fives(b, current=False):
            straight_fours = [sf for sf in get_fours(b) if sf.type == ThreatType.STRAIGHT_FOUR and sf.gain_square != t.gain_square]
            if straight_fours:
                # print("========================================fail")
                # print(b)
                # print(str(t))
                return False

        for cs in t.cost_squares:
            _b = b.copy()
            _b.move_index(cs)
            if not self.confirm_winning_line(_b, threats[1:]): return False
        return True

    def search(self, original, b=None, moves=[], current=True, depth=5):
        if depth == 0: return []

        # get threats
        if b is None: b = original
        threats = get_threats(b, current=current)

        # performance tracking
        if len(threats) == 0: self.nodes += 1
        self.execs += 1

        # return if winning threat in threats
        for t in threats:
            if t.type == ThreatType.FIVE or t.type == ThreatType.STRAIGHT_FOUR:
                if self.confirm_winning_line(original.copy(), [*moves, t]):
                    return [*moves, t]

        # search all dependent threats
        if len(moves) > 0:
            dependent = [t for t in threats if moves[-1].gain_square in t.rest_squares]
        else:
            dependent = threats
        for t in dependent:
            # play gain square, play all cost squares
            _b = b.copy()
            _b.force_index(t.gain_square, current=current)
            [_b.force_index(cost, current=not current) for cost in t.cost_squares]

            ans = self.search(original, _b, moves=[*moves, t], current=current, depth=depth-1)
            if ans: return ans

        # search all independent threats
        inline = set([1, 2, 15, 30, 16, 32, 14, 28])
        for i in range(len(threats)):
            for j in range(i + 1, len(threats)):
                t = threats[i]
                u = threats[j]
                if abs(t.gain_square - u.gain_square) in inline and t.gain_square not in u.cost_squares and u.gain_square not in t.cost_squares and set(u.cost_squares).isdisjoint(t.cost_squares):
                    _b = b.copy()
                    _b.force_index(t.gain_square, current=current)
                    [_b.force_index(cost, current=not current) for cost in t.cost_squares]

                    _b.force_index(u.gain_square, current=current)
                    [_b.force_index(cost, current=not current) for cost in u.cost_squares]

                    ans = self.search(original, _b, moves=[*moves, t, u], current=current, depth=depth-1)
                    if ans: return ans
        return []
