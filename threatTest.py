from gomoku.board import Board
from gomoku.threat.threat_search import get_fives, get_fours, get_threes, get_threats
from gomoku.player.threat_space import ThreatSpace
from gomoku.utils import to_row


p1 = [
    (4, 6),
    (5, 6),
    (7, 6),

    # (7, 6),
]
p2 = [
    (7, 1),
    (1, 5),
    (3, 5),
    # (3, 7),
]
# b = Board(b1=182715581618735388375710221972549795309907083264, b2=26959946667150639794758403540949547407647004528482569069719441113088, turns=16)
# b = Board(b1=316922321463614267476293976071, b2=28753546634630754380615942646379741989379916626753424690676020281344, turns=14)

b = Board(b1=7788603744127269971470931581730816, b2=118842243771396506390315925505, turns=6)
# b = Board(b1=15577207488254539942941863163461632, b2=20769266681644637892293645656129536, turns=6)
# b.force_move(8, 8)
# b = Board()
# b.moves(p1=p1, p2=p2)

b.print()

# [print(str(t)) for t in get_fours(b)]
t = ThreatSpace()
print([to_row(a) for a in t.search(b)])
# print(t.make_move(b))
