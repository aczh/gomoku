from gomoku.board import Board
from gomoku.threat.threat_search import get_fives, get_fours, get_threes

from gomoku.game import Game
# from gomoku.player.human import Human
# from gomoku.player.simple import Simple
# from gomoku.player.minimax import Minimax

# g = Game(Human(), Minimax())
# g.play()

p1_moves = [
    (3, 7),
    (2, 7),
    (3, 9),

]
p2_moves = [
    (12, 5),
    (13, 5),
    (14, 5),
]
b = Board()
b.moves(p1=p1_moves, p2=p2_moves)
# b = Board(b1=115792089237316195423570985008687907853269984665640564039457584007913129639935)
# straight fours board
# b = Board(b1=1569371220847030950282191793535370928631461435848467153016, b2=197460546927585330666561214562862828322343010451733252604562505728)

b.print()
print("=====")
# for t in get_fours(b):
for t in get_threes(b):
# for t in get_threes(b, current=False):
    print(str(t))
