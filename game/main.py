from gomoku import Game, Board
from gomoku.player import Human, Simple, ThreatSpace, Negamax

p1 = ThreatSpace()
p2 = Human()
g = Game(p1, p2)

g.play()
