from gomoku.board import Board
from gomoku.threat.threat_search import get_fives, get_fours

from gomoku.game import Game
# from gomoku.player.human import Human
# from gomoku.player.simple import Simple
# from gomoku.player.minimax import Minimax

# g = Game(Human(), Minimax())
# g.play()

p1_moves = [
    (0, 7),
    (1, 7),
    (2, 7),

]
p2_moves = [
    (2, 5),
    (3, 5),
    (4, 5),
]
b = Board()
b.moves(p1=p1_moves, p2=p2_moves)

# straight fours board
# b = Board(b1=1569371220847030950282191793535370928631461435848467153016, b2=197460546927585330666561214562862828322343010451733252604562505728)

b.print()
print("=====")
for t in get_fours(b):
# for t in get_fours(b, current=False):
    print(str(t))
