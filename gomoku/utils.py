from enum import Enum

class ThreatType(Enum):
    FIVE = 1
    STRAIGHT_FOUR = 2
    FOUR = 3
    THREE = 4
    BROKEN_THREE = 5

def to_row(index):
    return (index // 15, index % 15)

def to_index(r, c):
    return r * self.size + c
