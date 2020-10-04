from gomoku.board import Board
from gomoku.threat.threat_space import get_fours, get_threes, threat_space_search, get_straight_fours
from gomoku.utils import to_row, ThreatType

# b = Board(b1=680590695484625926093438556930779906048, b2=396155319976304968697169051648, turns=10)
# b = Board(b1=2787933468529643753549278615752325436801024, b2=12544254247361433409159635450619402997727232, turns=11)
b = Board(b1=85074486249991379969974003481027018752, b2=8362779454642241179290502190363056980099072, turns=18)
# b = Board(b1=170159356657930428656915835640124276736, b2=20769266669555379696147353909067776, turns=9)
# b.move(4, 6)
# b = Board(b1=446646568701890811025830444473897713664, b2=11683103721656334534779806651777024, turns=20)
print(b)
import cProfile
pr = cProfile.Profile()
pr.enable()

seqs = threat_space_search(b, max_seqs=5, depth=7)
for seq in seqs:
    print('---------SEQ--------')
    for t in seq:
        print(str(t))

pr.disable()
pr.print_stats(sort='time')
