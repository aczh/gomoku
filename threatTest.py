from gomoku.board import Board
from gomoku.threat.threat_space import get_fours, get_threes, threat_space_search, get_straight_fours
from gomoku.utils import to_row, ThreatType


import gmpy2
b = Board(b1=23037063802496884590169568565107503057583874975924630746556268551, b2=23589953333756809820333638239253801952324717697362898023789247885312, turns=40)
b.move(10, 2)
b.move(12, 9)
b.move(10, 3)
b.move(12, 10)
b.move(10, 5)
b.move(12, 11)
print(b)
[print(str(t)) for t in get_fours(b)]
# [print(str(t)) for t in get_straight_fours(b)]
# assert set([94, 214]) == set([t.gain_square for t in get_straight_fours(b)])
# b = Board(b1=170148972222669684030187449834553737216, b2=11682747164701579706989726983520256, turns=9)
# # b = Board(b1=23037063802496884590169568565107503057583874975924630746556268551, b2=23589953333756809820333638239253801952324717697362898023789247885312, turns=40)
# # b = Board(b1=15577049031929511414266676075560960, b2=41538771009091192349931938353512448, turns=6)
#
# # import cProfile
# # pr = cProfile.Profile()
# # pr.enable()
#
# print(b)
for seq in threat_space_search(b, max_seqs=5):
    print("\n\n\nSEQ:")
    for t in seq:
        print(str(t))
#
# # pr.disable()
# # pr.print_stats(sort='time')
