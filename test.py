from gomoku.board import Board
from gomoku.threat.threat_search import get_fours
# b = Board(b1=3368450625791641569852801897221545090422390492443040367981145065471, b2=0, turns=15)

p1 = [
]
p2 = [10, 11, 55, 57, 205, 208, 101, 102, 146, 148
]

b = Board(b1=1131284383158329154918172611346496335385136781746103479376572416, b2=0, turns=0)
b.moves(p1=p1, p2=p2)

# for r in range(15):
#     for c in range(15):
#         # if c < 11:
#         # if r < 11 and c < 11:
#         if r < 11 and c > 3:
#             b.force_move(r, c)
#
print(b)

# from gomoku.board import Board
# p1 = [
#     (0, 14),
#     (0, 13),
#     (0, 12),
#
#     (3, 14),
#     (3, 13),
#     (3, 11),
#
#     (6, 14),
#     (6, 13),
#     (6, 10),
#
#     (9, 14),
#     (9, 12),
#     (9, 10),
#
#     (13, 14),
#     (13, 12),
#     (13, 11),
# ]
# p2 = [
# ]
#
# b = Board()
# b.moves(p1=p1, p2=p2)
# print(b)
