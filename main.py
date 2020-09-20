from gomoku.board import Board
from gomoku.threat.threat_search import is_continuous

b = Board(size=15)
b.moves([])
#
# b.move(1, 1)
# b.move(4, 5)
# b.move(1, 2)
# b.move(6, 5)
# b.move(1, 3)
# b.move(7, 5)
# b.move(1, 4)
# b.move(8, 5)
# b.move(9, 5)
#
# b.print()
# print(get_fours_unblockable(b))
# print(get_fours_unblockable(b, current=False))

print(is_continuous(26, 90, 5))
print(is_continuous(19, 74, 5))
# print(continuous_threat(15, 19, 5))
# print(continuous_threat(14, 18, 5))

# 14, 15, 16, 17, 18

# 26, 42, 58, 74, 90

# 19, 33, 47, 61, 75
