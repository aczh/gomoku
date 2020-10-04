from gomoku.board import Board
from gomoku.threat.threat_space import get_fours, get_threes, threat_space_search, get_straight_fours
from gomoku.utils import to_row, ThreatType

# b = Board(b1=680590695484625926093438556930779906048, b2=396155319976304968697169051648, turns=10)
b = Board(b1=446646568701890811025830444473897713664, b2=11683103721656334534779806651777024, turns=20)
b.move(6, 7)
b.move(0, 0)
print(b)
import cProfile
pr = cProfile.Profile()
pr.enable()

seqs = threat_space_search(b, max_seqs=2)
for seq in seqs:
    print('---------SEQ--------')
    for t in seq:
        print(str(t))

# pr.disable()
# pr.print_stats(sort='time')
