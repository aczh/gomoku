import gmpy2

def _check(b, inc, num):
    for i in range(1, num):
        b = b & (b >> inc)
    return b

def has_five(board, current=True):
    '''
    Returns True if current player has a 5 in a row.
    ooooo
    '''
    b = board.get_board(current=current)

    # horizontal
    c = _check(b, 1, 5)
    index = 0
    while c:
        one = gmpy2.bit_scan1(c, index)
        if one is None:
            break
        if one % 15 < 11:
            return True
        index = one + 1

    # vertical
    c = _check(b, board.size, 5)
    if c: return True

    # d1
    c = _check(b, board.size + 1, 5)
    index = 0
    while c:
        one = gmpy2.bit_scan1(c, index)
        if one is None:
            break
        if one % 15 < 11:
            return True
        index = one + 1

    # d2
    c = _check(b, board.size - 1, 5)
    index = 0
    while c:
        one = gmpy2.bit_scan1(c, index)
        if one is None:
            break
        if one % 15 > 3:
            return True
        index = one + 1
    return False

def get_fours(board, current=True):
    '''
    Returns unblockable fours and blockable fours.
    Unblockable fours look like:
        -oooo-
    Blockable fours look like:
        xoooo-
        xooo-o
    '''
    b = board.get_board(current=current)
    return _check(b, 1, 4)
