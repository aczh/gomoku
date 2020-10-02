from gomoku.board import Board
from gomoku.threat.threat_search import get_fives, get_fours, get_threes, get_threats
from gomoku.player.threat_space import ThreatSpace
from gomoku.utils import to_row

'''
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
     ______________________________
 0  |- - - - - - - - - - - - - - -
 1  |- - - - - - - - - - - - - - -
 2  |- - - - - - - - - - - - - - -
 3  |- - - - - - - - - - - - - - -
 4  |- - - - - - - - - - - - - - -
 5  |- - - - x x x x - - - - - - -
 6  |- - - x - o x x o - - - - - -
 7  |- - - - o o o o x o - - - - -
 8  |- - - - - o x o - - - - - - -
 9  |- - - - - x x x x - - - - - -
10  |- - - - - - - o - - - - - - -
11  |- - - - - - - x x - - - - - -
12  |- - - - - - - - - - - - - - -
13  |- - - - - - - - - - - - - - -
14  |- - - - - - - - - - - - - - -
==================================
b1=182687704879069849201617767180651642938728644608, b2=17958932140429168763485909968367743450017487235579904, turns=10
Threatening line being played: [(6, 5), (8, 7), (10, 7), (7, 4), (7, 3)]
'''

b = Board(b1=29856023849225315921400728068816896, b2=85080976403187101590282738219192680448, turns=10)
# b.print()
b.move(6, 5)
b.move(0, 0)
b.print()
# [print(str(t)) for t in get_threats(b)]
win = ThreatSpace().search(b)
print([to_row(i) for i in win])
# b.move()
# b.move(0, 0)
# _b = b.copy()
# _b.force_move(7, 4)

# b = Board(b1=29856063463306573053569524840792064, b2=85080976403187101590282738219192680449, turns=12)
# b.print()
# print(ThreatSpace().search(b))
#
# t = ThreatSpace()
# print(ThreatSpace().make_move(b))
# print([to_row(a) for a in t.search(b)])





# from gomoku.board import Board
# from gomoku.threat.threat_search import get_fives, get_fours, get_threes, get_threats
# from gomoku.player.threat_space import ThreatSpace
# from gomoku.utils import to_row
#
#
# p1 = [
#     (4, 6),
#     (5, 6),
#     (7, 6),
#
#     # (7, 6),
# ]
# p2 = [
#     (7, 1),
#     (1, 5),
#     (3, 5),
#     # (3, 7),
# ]
# # b = Board(b1=182715581618735388375710221972549795309907083264, b2=26959946667150639794758403540949547407647004528482569069719441113088, turns=16)
# # b = Board(b1=316922321463614267476293976071, b2=28753546634630754380615942646379741989379916626753424690676020281344, turns=14)
#
# b = Board(b1=7788603744127269971470931581730816, b2=118842243771396506390315925505, turns=6)
# # b = Board(b1=15577207488254539942941863163461632, b2=20769266681644637892293645656129536, turns=6)
# # b.force_move(8, 8)
# # b = Board()
# # b.moves(p1=p1, p2=p2)
#
# b.print()
#
# # [print(str(t)) for t in get_fours(b)]
# t = ThreatSpace()
# print([to_row(a) for a in t.search(b)])
# # print(t.make_move(b))
