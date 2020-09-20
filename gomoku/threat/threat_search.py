import gmpy2

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

def get_threes(board, current=True):
    '''
    Returns threes:
        -ooo--
        -oo-o-
        -o-oo-
        --ooo-
    '''
    b = board.get_board(current=current)
    threes = []
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
        threats = set()
        for x in range(5):
            for y in range(x + 1, 5):
                r = [z for z in range(5) if z != x and z != y]
                bits = (b >> inc * r[0]) & (b >> inc * r[1]) & (b >> inc * r[2])
                ones = [
                    threats.update([o + x * inc, o + y * inc])
                    for o in get_ones(bits)
                    if is_continuous(o, inc, 5) and board.is_valid_index(o + x * inc) and board.is_valid_index(o + y * inc)
                ]
        threes.append(list(threats))

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

        threats = set()
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

            ones = [threats.add(o + x * inc) for o in get_ones(bits) if board.is_valid_index(o + x * inc) and is_continuous(o, inc, 5)]
        fours.append(list(threats))

    return fours

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
