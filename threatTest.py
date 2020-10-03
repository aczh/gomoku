from gomoku.board import Board
from gomoku.threat.threat_search import get_fives, get_fours, get_threes, get_threats
from gomoku.player.threat_space import ThreatSpace
from gomoku.utils import to_row

t = ThreatSpace()


p1 = [
    (7, 7),
    (8, 7),
    (8, 6),
    (8, 8),
    (6, 8),
    (5, 8),
    (5, 5),
    (5, 6),
    (6, 4),
]
p2 = [
    (6, 6),
    (6, 7),
    (6, 5),
    (7, 6),
    (8, 5),
    (5, 4),
    (7, 8),
    (8, 10),
    (5, 9),
]
b = Board(b1=595499334745233834758173289195407147008, b2=1403677744568336014931440404855653400576, turns=18)
# b.moves(p1=p1, p2=p2)

# [print(str(t)) for t in get_fours(b, current=False)]

print(b)
print([to_row(t.gain_square) for t in t.search(b)])

print(f'i: {t.i}')
print(f'nodes: {t.nodes}')
print(f'execs: {t.execs}')
