# from gomoku.board import Board
# from gomoku.threat.threat_search import get_fives, get_fours, get_threes, get_threats
# from gomoku.player.threat_space import ThreatSpace
# from gomoku.utils import to_row
#
# p1 = []
# p2 = []
#
# # p1 += [(i, i) for i in range(15)]
# # p1 += [(i + 1, i) for i in range(5)]
# # p1 += [(i, i + 1) for i in range(14)]
#
# p1 += [(14 - i - 2, i) for i in range(13)]
# p1 += [(14 - i - 1, i) for i in range(14)]
# p1 += [(14 - i, i) for i in range(15)]
# p1 += [(14 - i, i + 1) for i in range(14)]
# # 14, 1
# # 13, 2
# # 12, 3
#
# # 0, 14: 0, 1
#
# b = Board()
# b.moves(p1=p1, p2=p2)
# print(b)
#
# b.b1 = b.b1_d2_a
# # b.b1 = b.b1_d2_b
# print(b)

# from gomoku.board import Board
# from gomoku.threat.threat_space import threat_space_search
# from gomoku.utils import to_row
#
#
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
# b = Board()
#
# print(b)
# import cProfile
# pr = cProfile.Profile()
# pr.enable()
#
# print([to_row(t) for t in threat_space_search(b)])
#
# pr.disable()
# pr.print_stats(sort='time')
