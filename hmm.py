from gomoku.board import Board
from gomoku.threat.threat_search import get_fives, get_fours, get_threes, get_threats

from gomoku.game import Game
# from gomoku.player.human import Human
# from gomoku.player.simple import Simple
# from gomoku.player.minimax import Minimax

# g = Game(Human(), Minimax())
# g.play()

p1_moves = [
    (0, 0),
    (0, 1),
    (0, 2),

    (1, 5),
    (2, 6),

    (5, 8),
    (6, 8),

]
p2_moves = [
    (2, 8),
    (5, 9),
    (9, 8),

    (14, 14),
    (14, 10),
    (14, 6),
    (14, 1),
]
b = Board()
b.moves(p1=p1_moves, p2=p2_moves)
# b = Board(b1=115792089237316195423570985008687907853269984665640564039457584007913129639935)
# straight fours board
# b = Board(b1=1569371220847030950282191793535370928631461435848467153016, b2=197460546927585330666561214562862828322343010451733252604562505728)


b.force_move(0, 4, 8)
b.force_move(1, 3, 8)
b.force_move(1, 7, 8)
b.force_move(1, 8, 8)

b.print()
print("=====")
# for t in get_fours(b):
for t in get_threats(b):
# for t in get_threes(b, current=False):
    print(str(t))
