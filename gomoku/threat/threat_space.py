from .. threat.threat_search import get_fives, get_fours, get_threes, get_threats, has_five
from .. threat.threat import Three
from .. utils import to_row, ThreatType
from .. board import Board
import time

def confirm_winning_line(b, threats):
    if len(threats) == 0: return True

    if get_fives(b): return True
    if get_fives(b, current=False): return False

    t = threats[0]
    b.move_index(t.gain_square)

    if not get_fives(b, current=False):
        straight_fours = [sf for sf in get_fours(b) if sf.type == ThreatType.STRAIGHT_FOUR and sf.gain_square != t.gain_square]
        if straight_fours: return False

    for cs in t.cost_squares:
        _b = b.copy()
        _b.move_index(cs)
        if not confirm_winning_line(_b, threats[1:]): return False
    return True

def threat_space_search(b, moves=[], current=True, depth=10):
    nodes = 0
    execs = 0
    original = b.copy()
    def _search(b, moves=[], current=True, depth=50):
        if depth <= 0: return []

        # get threats
        threats = get_threats(b, current=current)

        # performance tracking
        nonlocal nodes
        nonlocal execs
        if len(threats) == 0:
            nodes += 1
        execs += 1

        if has_five(b):
            if confirm_winning_line(original.copy(), [*moves]):
                return [*moves]

        # return if winning threat in threats
        for t in threats:
            if t.type == ThreatType.FIVE or t.type == ThreatType.STRAIGHT_FOUR:
                if confirm_winning_line(original.copy(), [*moves, t]):
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

            ans = _search(_b, moves=[*moves, t], current=current, depth=depth-1)
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

                    ans = _search(_b, moves=[*moves, t, u], current=current, depth=depth-2)
                    if ans: return ans
        return []

    s = time.time()
    ans = _search(b, moves=moves, current=current, depth=depth)
    e = time.time()
    print(f'nodes: {nodes}, execs: {execs}, elapsed: {e - s}, {repr(original)}')
    return [t.gain_square for t in ans]
