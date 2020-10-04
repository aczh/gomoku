from gomoku.board import Board
# import gmpy2
#
# p1 = []
# p2 = []
#
# for r in range(15):
#     for c in range(15):
#         # if c < 11:
#         # if c < 10:
#         if c > 4 and r < 10:
#         # if c < 9:
#         # if c < 9 and r < 9:
#         # if r < 11 or c <=3:
#             p1.append((r, c))
# b = Board()
# b.moves(p1=p1, p2=p2)
# print(b)
# print(b.b1)


from gomoku.threat.threat_masks import threat_mask

b = Board()
b.b1 = threat_mask[7][16]
print(b)
