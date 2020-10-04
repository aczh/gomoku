from gomoku.board import Board
from gomoku.threat.threat_space import threat_space_search
from gomoku.utils import to_row


# p1 = [
#     (7, 7),
#     (8, 7),
#     (8, 6),
#     (8, 8),
#     (6, 8),
#     (5, 8),
#     (5, 5),
#     (5, 6),
#     (6, 4),
# ]
# p2 = [
#     (6, 6),
#     (6, 7),
#     (6, 5),
#     (7, 6),
#     (8, 5),
#     (5, 4),
#     (7, 8),
#     (8, 10),
#     (5, 9),
# ]
b = Board(b1=255216967487562382425159486070155378688, b2=396140812571321687967719751680, turns=4)
# b.moves(p1=p1, p2=p2)

print(b)
import cProfile
pr = cProfile.Profile()
pr.enable()

print([to_row(t) for t in threat_space_search(b)])

pr.disable()
pr.print_stats(sort='time')
