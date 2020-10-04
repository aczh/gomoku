from .. threat.threat_search import get_fives, get_fours, get_threes, get_threats, has_five, get_straight_fours
from .. threat.threat import Three
from .. utils import to_row, ThreatType
from .. board import Board
import time

def confirm_winning_line(b, threats):
    '''Confirms a string of threats leads to a win.'''
    if len(threats) == 0: return True
    t = threats[0]

    # if we have a win, return True.
    if get_fives(b): return True
    # if the enemy has a five threat we must counter that disrupts our threat chain, return False
    if [f for f in get_fives(b, current=False) if f.gain_square != t.gain_square]: return False

    # place the gain square of the first threat
    b.force_index(t.gain_square)

    # only worry about straight_four threats if we aren't threatening a five.
    if t.type < ThreatType.FOUR:
        fours = get_fours(b, current=False)

        if [sf for sf in get_straight_fours(b, current=False) if sf.gain_square != t.gain_square]: return False

        opponent_fours = get_fours(b, current=False)
        if opponent_fours:
            for ot in opponent_fours:
                _b = b.copy()
                _b.force_index(ot.gain_square)
                _b.force_index(ot.cost_squares[0], current=False)
                _b.force_undo_index(t.gain_square)
                if not confirm_winning_line(_b, threats): return False
            return True

        # opponent_fours = get_fours(b, current=False)
        #
        # for f in opponent_fours:
        #     if f.type == ThreatType.STRAIGHT_FOUR and f.gain_square != t.gain_square: return False
        #
        # if opponent_fours:
        #     for ot in opponent_fours:
        #         _b = b.copy()
        #         _b.force_index(ot.gain_square)
        #         _b.force_index(ot.cost_squares[0], current=False)
        #         _b.force_undo_index(t.gain_square)
        #         if not confirm_winning_line(_b, threats): return False
        #     return True

    # the only moves the opponent can make are:
    # moves that directly block the incoming threat
    # five threats IF we aren't threatening a five
    for cs in t.cost_squares:
        _b = b.copy()
        _b.force_index(cs, current=False)
        if not confirm_winning_line(_b, threats[1:]): return False
    return True

def threat_space_search(b, moves=[], current=True, depth=6, max_seqs=1, VERBOSE=0):
    nodes = 0
    execs = 0
    original = b.copy()
    seqs = []
    def _search(b, moves=[], current=True, depth=50):
        if depth <= 0: return

        # get threats
        threats = get_threats(b, current=current)

        # performance tracking
        nonlocal nodes
        nonlocal execs
        if len(threats) == 0:
            nodes += 1
        execs += 1

        # return if winning threat is found
        if has_five(b):
            if confirm_winning_line(original.copy(), moves):
                seqs.append(moves)
                return
        for t in threats:
            if t.type == ThreatType.FIVE or t.type == ThreatType.STRAIGHT_FOUR:
                if confirm_winning_line(original.copy(), [*moves, t]):
                    seqs.append([*moves, t])
                    return

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

            _search(_b, moves=[*moves, t], current=current, depth=depth-1)
            if len(seqs) >= max_seqs: return


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

                    _search(_b, moves=[*moves, t, u], current=current, depth=depth-2)
                    if len(seqs) >= max_seqs: return

    s = time.time()
    _search(b, moves=moves, current=current, depth=depth)
    e = time.time()
    if VERBOSE: print(f'nodes: {nodes}, execs: {execs}, elapsed: {e - s}, {repr(original)}')
    return seqs
