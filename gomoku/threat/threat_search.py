import gmpy2
from . import threat
from .. import utils
from .. utils import ThreatType, is_continuous, get_ones


def get_threats(board, current=True):
    return get_threes(board, current=current) + get_fours(board, current=current) + get_fives(board, current=current)

def get_threes(board, current=True):
    b = board.get_board(current=current)
    ret = []
    for inc in [1, board.size, board.size + 1, board.size - 1]:
        cur = {}
        # =============
        # - - o o o - -
        # =============
        # - - - o o - -
        # - - o - o - -
        # - - o o - - -
        for x in range(3):
            r = [z + 2 for z in range(3) if z != x]
            bits = (b >> inc * r[0]) & (b >> inc * r[1])
            e = [z for z in range(7) if z not in r]

            for o in get_ones(bits):
                if is_continuous(o, inc, 7) and all([board.is_valid_index(o + inc * i) for i in e]):
                    gain = o + (x + 2) * inc
                    rest = [o + (i + 2) * inc for i in range(3) if i != x]
                    cost = [o + inc, o + inc * 5]
                    cur[gain] = threat.Three(gain=gain, cost=cost, rest=rest)

        # 12: - o o ! ? -
        # 13: - o ! o ? -
        # 14: - o ? ? o -
        # 23: - ! o o ! -
        # 24: - ? o ! o -
        # 34: - ? ! o o -
        lookup = {
            (1, 2): [[ [3, 4] ], [ [4, 3] ]],
            (1, 3): [[ [2, 4] ], [ [4, 2] ]],
            (1, 4): [[], [ [2, 3], [3, 2] ]],
            (2, 3): [[ [1, 4], [4, 1] ], []],
            (2, 4): [[ [3, 1] ], [ [1, 3] ]],
            (3, 4): [[ [2, 1] ], [ [1, 2] ]],
        }
        for x in range(1, 4):
            for y in range(x + 1, 5):
                e = [z for z in range(6) if z != x and z != y]
                bits = (b >> inc * x) & (b >> inc * y)
                for o in get_ones(bits):
                    if is_continuous(o, inc, 6) and all([board.is_valid_index(o + inc * i) for i in e]):
                        for gain, cost in lookup[(x, y)][0]:
                            gain_index = o + gain * inc
                            if gain_index not in cur:
                                cur[gain_index] = threat.Three(
                                    gain=gain_index,
                                    cost=[o, o + inc * 5, o + inc * cost],
                                    rest=[o + x * inc, o + y * inc],
                                )
                        for gain, cost in lookup[(x, y)][1]:
                            gain_index = o + gain * inc
                            if gain_index not in cur:
                                cur[gain_index] = threat.BrokenThree(
                                    gain=gain_index,
                                    cost=[o, o + inc * 5, o + inc * cost],
                                    rest=[o + x * inc, o + y * inc],
                                )
        ret += cur.values()
    return ret

def get_fours(board, current=True):
    b = board.get_board(current=current)
    ret = []
    for inc in [1, board.size, board.size + 1, board.size - 1]:
        # 01: - - o o o
        # 02: - o - o o
        # 03: - o o - o
        # 04: - o o o -

        # 12: o - - o o
        # 13: o - o - o
        # 14: o - o o -

        # 23: o o - - o
        # 24: o o - o -

        # 34: o o o - -
        cur = {}
        for x in range(5):
            for y in range(x + 1, 5):
                r = [z for z in range(5) if z != x and z != y]
                bits = (b >> inc * r[0]) & (b >> inc * r[1]) & (b >> inc * r[2])
                for o in get_ones(bits):
                    i1 = o + x * inc
                    i2 = o + y * inc
                    if is_continuous(o, inc, 5) and board.is_valid_index(i1) and board.is_valid_index(i2):
                        # check for straight fours
                        if x == 0 and y == 1 and board.is_valid_index(o + 5 * inc):
                            cur[i2] = threat.StraightFour(o, inc, i2, i1)
                            continue
                        if x == 3 and y == 4 and board.is_valid_index(o - inc):
                            cur[i1] = threat.StraightFour(o, inc, i1, i2)
                            continue

                        # regular fours
                        if i1 in cur:
                            if cur[i1].type != ThreatType.STRAIGHT_FOUR:
                                cur[i1].cost_squares.append(i2)
                        else:
                            cur[i1] = threat.Four(o, inc, i1, i2)

                        if i2 in cur:
                            if cur[i2].type != ThreatType.STRAIGHT_FOUR:
                                cur[i2].cost_squares.append(i1)
                        else:
                            cur[i2] = threat.Four(o, inc, i2, i1)
        ret += cur.values()
    return ret

def get_fives(board, current=True):
    b = board.get_board(current=current)
    ret = []
    for inc in [1, board.size, board.size + 1, board.size - 1]:
        shifts = [0, 1, 2, 3, 4]
        # 0: - o o o o
        # 1: o - o o o
        # 2: o o - o o
        # 3: o o o - o
        # 4: o o o o -

        for x in shifts:
            if x == 0:
                bits = (b >> inc) & (b >> inc * 2) & (b >> inc * 3) & (b >> inc * 4)
            elif x == 1:
                bits = b & (b >> inc * 2) & (b >> inc * 3) & (b >> inc * 4)
            elif x == 2:
                bits = b & (b >> inc * 1) & (b >> inc * 3) & (b >> inc * 4)
            elif x == 3:
                bits = b & (b >> inc * 1) & (b >> inc * 2) & (b >> inc * 4)
            elif x == 4:
                bits = b & (b >> inc * 1) & (b >> inc * 2) & (b >> inc * 3)
            for o in get_ones(bits):
                if board.is_valid_index(o + x * inc) and is_continuous(o, inc, 5):
                    ret.append(threat.Five(o, inc, o + x * inc))
    return ret


def has_five(board, current=True):
    '''
    Returns True if current player has a 5 in a row.
    ooooo
    '''
    b = board.get_board(current=current)

    for inc in [1, board.size, board.size + 1, board.size - 1]:
        bits = b & (b >> inc) & (b >> inc * 2) & (b >> inc * 3) & (b >> inc * 4)
        threats = [o for o in get_ones(bits) if is_continuous(o, inc, 5)]
        if threats:
            return True
    return False
