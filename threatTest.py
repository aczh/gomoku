from gomoku.board import Board
from gomoku.threat.threat_search import get_fives, get_fours, get_threes, get_threats

from gomoku.player.threat_space import ThreatSpace

# p1_moves = [
#     (5, 5),
#     (5, 6),
#     (5, 7),
# ]
# p2_moves = [
#     (6, 8),
#     (6, 9),
#     # (6, 10),
# ]
p1_moves = [
    (0, 0),
    (0, 1),
    (0, 2),

    (1, 5),
    (2, 6),

    (5, 8),
    (6, 8),

]
p2_moves = [
    (2, 8),
    (5, 9),
    (9, 8),

    (14, 14),
    (14, 10),
    (14, 6),
    (14, 1),
]
b = Board()
b.moves(p1=p1_moves, p2=p2_moves)
b.turns=14

b.print()
t = ThreatSpace()
print(t.make_move(b))
