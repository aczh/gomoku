from enum import IntEnum
import gmpy2

class ThreatType(IntEnum):
    FIVE = 5
    STRAIGHT_FOUR = 4
    FOUR = 3
    THREE = 2
    BROKEN_THREE = 1

def to_row(index):
    return (index // 15, index % 15)

def to_index(r, c):
    return r * self.size + c

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
