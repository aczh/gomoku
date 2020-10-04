import gmpy2
from . import threat
from .. import utils
from .. utils import ThreatType, get_ones, to_row
from . threat_masks import threat_mask

def get_threats(board, current=True):
    threats = get_fives(board, current=current) +  get_fours(board, current=current) + get_threes(board, current=current)
    return threats

def get_threes(board, current=True):
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
            emp = [z for z in range(7) if z not in r]

            e_bits = (board.e >> inc * emp[0]) & (board.e >> inc * emp[1]) & (board.e >> inc * emp[2]) & (board.e >> inc * emp[3]) & (board.e >> inc * emp[4])

            bits = (b >> inc * r[0]) & (b >> inc * r[1])
            bits = bits & threat_mask[7][inc]
            bits = bits & e_bits

            for o in get_ones(bits):
                gain = o + (x + 2) * inc
                rest = [o + (i + 2) * inc for i in range(3) if i != x]
                cost = [o + inc, o + inc * 5]
                cur[gain] = threat.Three(gain=gain, cost=cost, rest=rest)

        for x in range(1, 4):
            for y in range(x + 1, 5):
                emp = [z for z in range(6) if z != x and z != y]

                e_bits = (board.e >> inc * emp[0]) & (board.e >> inc * emp[1]) & (board.e >> inc * emp[2]) & (board.e >> inc * emp[3])

                bits = (b >> inc * x) & (b >> inc * y)
                bits = bits & threat_mask[6][inc]
                bits = bits & e_bits

                for o in get_ones(bits):
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

def get_straight_fours(board, current=True):
    b = board.get_board(current=current)
    ret = []
    ################
    # STRAIGHT FOURS
    ################
    # - ! o o o -
    # - o ! o o -
    # - o o ! o -
    # - o o o ! -
    straight_four_lookup = [
        [ [0, 1, 5], [2, 3, 4] ],
        [ [0, 2, 5], [1, 3, 4] ],
        [ [0, 3, 5], [1, 2, 4] ],
        [ [0, 4, 5], [1, 2, 3] ],
    ]

    for inc in [1, board.size, board.size + 1, board.size - 1]:
        for emp, occ in straight_four_lookup:
            e_bits = (board.e >> inc * emp[0]) & (board.e >> inc * emp[1]) & (board.e >> inc * emp[2])

            bits = (b >> inc * occ[0]) & (b >> inc * occ[1]) & (b >> inc * occ[2])
            bits = bits & threat_mask[6][inc]
            bits = bits & e_bits

            for o in get_ones(bits):
                gain_index = o + inc * emp[1]
                ret.append(threat.StraightFour(o, inc, o + inc * emp[1], o))
    return ret

def get_fours(board, current=True):
    b = board.get_board(current=current)
    ret = []

    ################
    # STRAIGHT FOURS
    ################
    # - ! o o o -
    # - o ! o o -
    # - o o ! o -
    # - o o o ! -
    straight_four_lookup = [
        [ 1, [0, 1, 5], [2, 3, 4] ],
        [ 2, [0, 2, 5], [1, 3, 4] ],
        [ 3, [0, 3, 5], [1, 2, 4] ],
        [ 4, [0, 4, 5], [1, 2, 3] ],
    ]


    ################
    # FOURS
    ################
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
    four_lookup = [
        [ [0, 1], [2, 3, 4] ],
        [ [0, 2], [1, 3, 4] ],
        [ [0, 3], [1, 2, 4] ],
        [ [0, 4], [1, 2, 3] ],
        [ [1, 2], [0, 3, 4] ],
        [ [1, 3], [0, 2, 4] ],
        [ [1, 4], [0, 2, 3] ],
        [ [2, 3], [0, 1, 4] ],
        [ [2, 4], [0, 1, 3] ],
        [ [3, 4], [0, 1, 2] ],
    ]
    for inc in [1, board.size, board.size + 1, board.size - 1]:
        cur = {}
        for gain, emp, occ in straight_four_lookup:
            e_bits = (board.e >> inc * emp[0]) & (board.e >> inc * emp[1]) & (board.e >> inc * emp[2])\

            bits = (b >> inc * occ[0]) & (b >> inc * occ[1]) & (b >> inc * occ[2])
            bits = bits & threat_mask[6][inc]
            bits = bits & e_bits

            for o in get_ones(bits):
                gain_index = o + inc * emp[1]
                cur[gain_index] = threat.StraightFour(o, inc, gain_index, o)

        for emp, occ in four_lookup:
            e_bits = (board.e >> inc * emp[0]) & (board.e >> inc * emp[1])

            bits = (b >> inc * occ[0]) & (b >> inc * occ[1]) & (b >> inc * occ[2])
            bits = bits & threat_mask[5][inc]
            bits = bits & e_bits

            for o in get_ones(bits):
                i1 = o + emp[0] * inc
                i2 = o + emp[1] * inc
                if i1 not in cur:
                    cur[i1] = threat.Four(o, inc, i1, i2)
                if i2 not in cur:
                    cur[i2] = threat.Four(o, inc, i2, i1)
        ret += cur.values()
    return ret

def get_fives(board, current=True):
    b = board.get_board(current=current)

    # 0: - o o o o
    # 1: o - o o o
    # 2: o o - o o
    # 3: o o o - o
    # 4: o o o o -
    lookup = [
        [ 0, [1, 2, 3, 4] ],
        [ 1, [0, 2, 3, 4] ],
        [ 2, [0, 1, 3, 4] ],
        [ 3, [0, 1, 2, 4] ],
        [ 4, [0, 1, 2, 3] ],
    ]

    ret = []
    for inc in [1, board.size, board.size + 1, board.size - 1]:
        for emp, occ in lookup:
            bits = (b >> inc * occ[0]) & (b >> inc * occ[1]) & (b >> inc * occ[2]) & (b >> inc * occ[3]) & threat_mask[5][inc]
            for o in get_ones(bits):
                gain_square = o + emp * inc
                if board.is_valid_index(gain_square):
                    ret.append(threat.Five(o, inc, gain_square))
    return ret


def has_five(board, current=True):
    '''
    Returns True if current player has a 5 in a row.
    ooooo
    '''
    b = board.get_board(current=current)
    for inc in [1, board.size, board.size + 1, board.size - 1]:
        bits = b & (b >> inc) & (b >> inc * 2) & (b >> inc * 3) & (b >> inc * 4)
        bits = bits & threat_mask[5][inc]
        if bits: return True
    return False
