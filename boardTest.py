from gomoku.board import Board
from gomoku.threat.threat_search import get_fives, get_fours, get_threes, get_threats
from gomoku.player.threat_space import ThreatSpace
from gomoku.utils import to_row

p1 = [

    # (1, 0),
    # (1, 1),
    # (1, 2),
    # (1, 3),
    # (1, 4),
    # (1, 5),
    # (1, 6),
    # (1, 7),
    # (1, 8),
    # (1, 9),
    # (1, 10),
    # (1, 11),
    # (1, 12),
    # (1, 13),
    # (1, 14),
]
p1 = [(14 - i, i) for i in range(15)]
p2 = [
    # (14, 3),
    # (13, 13),
    # (12, 12),
    # (11, 11),
    # (10, 10),
    # (9, 9),
    # (8, 8),
]

b = Board()
b.moves(p1=p1, p2=p2)
# b.b1 = b.b1_t
# b.b1 = b.b1_c
# b.b1 = b.b1_d1
b.b1 = b.b1_d2
print(b)

# 14, 1: 0, 1
# 13, 2: 0, 2
# 12, 3: 0, 3
