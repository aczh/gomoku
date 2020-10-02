from .. threat.threat_search import get_fives, get_fours, get_threes, get_threats
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
            score = len(get_threes(_b)) * 5 + len(get_threes(_b, current=False)) * 3
            score += self.touching(b, move)
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

        # block straight 4
        forced = [t for t in get_fours(b, current=False) if t.type == ThreatType.STRAIGHT_FOUR]
        if forced: return forced[0].gain_square

        return None

    def valid_moves(self, b):
        return [i for i in range(225) if b.is_valid_index(i)]

    def make_move(self, b):
        if b.turns == 0: return (7, 7)

        forced = self.forced_moves(b)
        if forced:
            print(f'Making forced move...: {to_row(forced)}')
            return forced

        if self.winning_line:
            if VERBOSE: print(f'Saved winning line being played: {[to_row(move) for move in self.winning_line[::-1]]}')
            return self.winning_line.pop()


        # search for winnig line
        moves = self.search(b)
        if moves:
            if VERBOSE: print(f'Winning line being played: {[to_row(move) for move in moves]}')
            self.winning_line = moves[::-1]
            return self.winning_line.pop()

        # search for winning line in opponent's board
        moves = self.search(b, current=False)
        if moves:
            if VERBOSE: print(f'Winning line being blocked: {[to_row(move) for move in moves]}')
            return moves[0]

        # make a move based on simple heuristic
        best_moves = [tup[1] for tup in self.score_moves(b)[:10]]
        for move in best_moves:
            _b = b.copy()
            _b.force_index(move)
            moves = self.search(_b)
            if moves:
                if VERBOSE: print(f'Threatening line being played: {[to_row(move) for move in moves]}')
                return moves[0]

        print('Random move...')
        return random.choice(best_moves)

    def confirm_winning_line(self, b, moves):
        return True

    def search(self, b, seen=set(), moves=[], current=True, depth=6):
        if depth < 0: return

        # only consider created threats
        new_threats = set(get_threats(b, current=current))
        diff = new_threats.difference(seen)
        seen = new_threats.union(seen)

        # for t in seen:
        for t in diff:
            if t.type == ThreatType.FIVE or t.type == ThreatType.STRAIGHT_FOUR:
                b.print()
                return [*moves, t.gain_square]

            # play the threat
            # play all possible counter moves to the threat
            _b = b.copy()
            _b.force_index(t.gain_square, current=current)
            for cost in t.cost_squares:
                _b.force_index(cost, current=not current)

            ans = self.search(_b, seen, moves=[*moves, t.gain_square], current=current, depth=depth-1)
            if ans and self.confirm_winning_line(b, moves): return ans

        for t in new_threats:
            _b = b.copy()
            if _b.is_valid_index(t.gain_square):
                _b.force_index(t.gain_square)
                for cost in t.cost_squares:
                    _b.force_index(cost, current=not current)

                ans = self.search(_b, seen, moves=[*moves, t.gain_square], current=current, depth=depth-1)
                if ans and self.confirm_winning_line(b, moves): return ans
