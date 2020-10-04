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

    def score_moves(self, b, limit_moves=None):
        if limit_moves is None:
            limit_moves = self.valid_moves(b)
        scored_moves = []
        for move in limit_moves:
            _b = b.copy()
            _b.force_index(move)
            score = 0
            score += 1.25 * (len(get_fours(_b, current=True)) + len(get_threes(_b, current=True)))
            score -= len(get_fours(_b, current=False)) + len(get_threes(_b, current=False))
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
            if VERBOSE: print(f'Saved winning line being played: {[to_row(t.gain_square) for t in self.winning_line[::-1]]}')
            return self.winning_line.pop().gain_square

        # search for winning line
        moves = threat_space_search(b)
        if moves:
            if VERBOSE: print(f'Winning line being played: {[to_row(t.gain_square) for t in moves[0]]}')
            self.winning_line = moves[0][::-1]
            return self.winning_line.pop().gain_square

        # # search for winning line in opponent's board
        moves = threat_space_search(b, current=False, max_seqs=5)
        limit_moves = None
        if moves:
            for seq in moves:
                workable_moves = set()
                print(f'Enemy winning seq------------')
                for t in seq:
                    workable_moves.add(t.gain_square)
                    if t.type == ThreatType.STRAIGHT_FOUR:
                        workable_moves.update([sq for sq in t.rest_squares if b.is_valid_index(sq)])
                        workable_moves.add(2 * t.rest_squares[0] - t.rest_squares[1])
                        workable_moves.add(2 * t.rest_squares[2] - t.rest_squares[1])
                    else:
                        workable_moves.update(t.cost_squares)

                    print(str(t))

                if limit_moves is None:
                    limit_moves = workable_moves
                else:
                    limit_moves = limit_moves & workable_moves

            print(f'Moves limited to: {[to_row(move) for move in limit_moves]}')

        # make a move based on simple heuristic
        score_moves = self.score_moves(b, limit_moves=limit_moves)
        best_moves = [tup[1] for tup in score_moves][:10]
        threatening_moves = []
        for move in best_moves:
            _b = b.copy()
            _b.force_index(move)
            tss = threat_space_search(_b)
            if tss:
                moves = [move]
                [moves.append(t.gain_square) for t in tss[0]]
                if VERBOSE: print(f'Threatening line: {[to_row(t) for t in moves]}')
                threatening_moves.append(move)
        if threatening_moves:
            return random.choice(threatening_moves)

        print('Random move...')
        return random.choice(best_moves)
        # return random.choice([tup[1] for tup in score_moves if tup[0] == score_moves[0][0]][:10])
