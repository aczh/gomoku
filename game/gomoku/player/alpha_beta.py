from .. threat.threat_search import get_fives, get_fours, get_threes, has_five
from .. threat.threat_space import threat_space_search
from .. threat.threat import ThreatType

class AlphaBeta:
    def request_move(self, b, game):
        move = self.make_move(b)
        game.make_move(move)

    def make_move(self, b):
        print('==================')
        print(self.eval_board(b))

        if b.turns == 0: return (7, 7)
        if b.turns == 1:
            if b.is_valid_move(7, 7): return (7, 7)
            return (6, 6)

        best_val = -1001
        best_move = None

        for move in self.score_moves(b)[:5]:
            _b = b.copy()
            _b.move_index(move)
            val = self.alpha_beta(_b, multiplier=-1)
            if val > best_val:
                best_val = val
                best_move = move
        print(best_move)
        return best_move

    def eval_board(self, b, current=True):
        if has_five(b) or threat_space_search(b):
            return 1000

        if has_five(b, current=False):
            return -1000

        cur_player_score = len(get_fours(b)) * 10 + len(get_threes(b)) * 5
        other_player_score = len(get_fours(b, current=False)) * 10 + len(get_threes(b, current=False)) * 5
        return cur_player_score * 1.5 - other_player_score

    def alpha_beta(self, b, depth=2, alpha=-1000, beta=1000, multiplier=1):
        if depth <= 0:
            return self.eval_board(b) * multiplier

        val = -1000
        for move in self.score_moves(b)[:5]:
            _b = b.copy()
            _b.move_index(move)
            val = max(val, -self.alpha_beta(_b, depth=depth - 1, alpha=-beta, beta=-alpha, multiplier=-multiplier))
            alpha = max(alpha, val)
            if alpha >= beta:
                break
        return val

    def score_moves(self, b):
        # make 5
        forced = get_fives(b)
        if forced: return [forced[0].gain_square]

        # block 5
        forced = get_fives(b, current=False)
        if forced: return [forced[0].gain_square]

        # make straight 4
        forced = [t for t in get_fours(b) if t.type == ThreatType.STRAIGHT_FOUR]
        if forced: return [forced[0].gain_square]

        scored_moves = []
        for move in self.valid_moves(b):
            _b = b.copy()
            _b.force_index(move)
            score = 0
            score += len(get_fours(_b)) * 4 + len(get_threes(_b)) * 3
            score *= 1.5
            score -= len(get_fours(_b, current=False)) * 4 + len(get_threes(_b, current=False)) * 3
            scored_moves.append((score, move))
        scored_moves.sort(reverse=True)
        return [tup[1] for tup in scored_moves]

    def valid_moves(self, b):
        # get all possible moves on the board
        moves = [
            r * 15 + c
            for r in range(b.size) for c in range(b.size)
            if b.is_valid_move(r, c)
        ]
        return moves
