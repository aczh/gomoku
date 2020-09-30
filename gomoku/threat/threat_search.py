import gmpy2
from . import threat
from .. import utils
from .. utils import ThreatType

def is_continuous(start, inc, length):
    end = start + inc * (length - 1)
    return abs(end % 15 - start % 15) < length

def get_ones(num):
    '''Get indices of ones.'''
    indices = []
    i = 0
    while num:
        one = gmpy2.bit_scan1(num, i)
        if one is None:
            break
        indices.append(one)
        i = one + 1
    return indices

def get_fives(board, current=True):
    '''
    Returns five threats.
    '''
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

def get_fours(board, current=True):
    '''
    Returns four threats:
        -ooo--
        -oo-o-
        -o-oo-
        --ooo-
    '''
    b = board.get_board(current=current)
    ret = {}
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
                            ret[i2] = threat.StraightFour(o, inc, i2, i1)
                            continue
                        if x == 3 and y == 4 and board.is_valid_index(o - inc):
                            ret[i1] = threat.StraightFour(o, inc, i1, i2)
                            continue

                        # regular fours
                        if i1 in ret:
                            if ret[i1].type != ThreatType.STRAIGHT_FOUR:
                                ret[i1].cost_squares.append(i2)
                        else:
                            ret[i1] = threat.Four(o, inc, i1, i2)

                        if i2 in ret:
                            if ret[i2].type != ThreatType.STRAIGHT_FOUR:
                                ret[i2].cost_squares.append(i1)
                        else:
                            ret[i2] = threat.Four(o, inc, i2, i1)
    return ret.values()

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
