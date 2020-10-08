from gomoku import Board, Game
from gomoku.player import Human, Simple, ThreatSpace, Negamax

g = Game(ThreatSpace(), Human())
# g = Game(Simple(), Simple())
# g = Game(Human(), Human())
# g = Game(ThreatSpace(), Human())
# g = Game(Human(), ThreatSpace())

g.play()
