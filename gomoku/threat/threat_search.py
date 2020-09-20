import gmpy2

def _fives(b, inc):
    '''ooooo'''
    return b & (b >> inc) & (b >> inc * 2) & (b >> inc * 3) & (b >> inc * 4)

def _fours(b, inc):
    '''oooo'''
    return b & (b >> inc) & (b >> inc * 2) & (b >> inc * 3)

def _fours_broken(b, inc):
    '''
    o-ooo
    oo-oo
    ooo-o
    '''
    x = b & (b >> inc * 2) & (b >> inc * 3) & (b >> inc * 4)
    y = b & (b >> inc) & (b >> inc * 3) & (b >> inc * 4)
    z = b & (b >> inc) & (b >> inc * 2) & (b >> inc * 4)
    return x, y, z

def _threes(b, inc):
    '''-ooo-'''
    return b & (b >> inc) & (b >> inc * 2)

def _threes_broken(b, inc):
    '''
    -o-oo-
    -oo-o-
    '''
    x = b & (b >> inc * 2) & (b >> inc * 3)
    y = b & (b >> inc) & (b >> inc * 3)
    return x, y

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

def _validate_threat(num, inc, length=5, board_size=15):
    indices = get_ones(num)
    if inc == board_size:
        return indices
    return [i for i in indices if is_continuous(i, inc, 5)]

def get_threes(board, current=True):
    '''
    Returns threes:
        -ooo-
        -o-oo-
        -oo-o-
    '''
    b = board.get_board(current=current)

    threes = []

    for inc in [1, board.size, board.size - 1, board.size + 1]:
        candidates = get_ones(_threes(b, inc))
        for c in candidates:
            m1 = board.is_valid_index(c - inc)
            m2 = board.is_valid_index(c + 3 * inc)
            if m1 and m2 and is_continuous(c - inc, inc, 4):
                threes.append([c - inc, c + 3 * inc])

        for i, candidates in enumerate(_threes_broken(b, inc)):
            for c in candidates:
                m1 = board.is_valid_index(c - inc)
                m2 = board.is_valid_index(c + (i + 1) * inc)
                m3 = board.is_valid_index(c + 4 * inc)
                if m2:
                    threat = []
                    if m1 and is_continuous(c - inc, inc, 2):
                        threat.append(c - inc)
                    if m2 and is_continuous(c, inc, 4):
                        threat.append(c + 4 * inc)
                    threes.append(threat)
        return threes

def get_fours(board, current=True):
    b = board.get_board(current=current)
    fours = []
    for inc in [1, board.size, board.size + 1, board.size - 1]:
        shifts = [0, 1, 2, 3, 4]
        # 0: - o o o o
        # 1: o - o o o
        # 2: o o - o o
        # 3: o o o - o
        # 4: o o o o -

        threats = []
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

            ones = [o + x * inc for o in get_ones(bits) if board.is_valid_index(o + x * inc) and is_continuous(o, inc, 5)]
            threats += ones
        fours.append(threats)

    return fours


# def get_fours(board, current=True):
#     '''
#     Returns unblockable fours:
#         -oooo-
#     Returns blockable fours:
#         xoooo-
#         xooo-o
#         xoo-oo
#         xo-ooo
#     '''
#     b = board.get_board(current=current)
#
#     fours_unblockable = []
#     fours_blockable = []
#     for inc in [1, board.size, board.size - 1, board.size + 1]:
#         unblockable = []
#         blockable = []
#
#         candidates = get_ones(_fours(b, inc))
#         for c in candidates:
#             m1 = board.is_valid_index(c - inc)
#             m2 = board.is_valid_index(c + 4 * inc)
#             if m1 and m2:
#                 if is_continuous(c - inc, inc, 6):
#                     unblockable.append([c - inc, c + 4 * inc])
#                 else:
#                     if is_continuous(c - inc, inc, 2):
#                         blockable.append([c - inc])
#                     else:
#                         blockable.append([c + 4 * inc])
#             elif m1 or m2:
#                 blockable.append([c - inc, c + 4 * inc])
#
#         for i, bits in enumerate(_fours_broken(b, inc)):
#             candidates = _validate_threat(bits, inc, board.size)
#             for c in candidates:
#                 move = c + (i + 1) * inc
#                 if board.is_valid_index(move):
#                     blockable.append(move)
#
#         fours_unblockable.append(unblockable)
#         fours_blockable.append(blockable)
#     return fours_unblockable, fours_blockable

def has_five(board, current=True):
    '''
    Returns True if current player has a 5 in a row.
    ooooo
    '''
    b = board.get_board(current=current)

    # vertical
    c = _fives(b, board.size)
    if c: return True

    # check for horizontal, d2, d1 (in that order)
    for inc in [1, board.size - 1, board.size + 1]:
        c = _fives(b, inc)
        if _validate_threat(c, inc, board.size):
            return True
    return False
