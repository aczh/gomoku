from gomoku.game import Game
from gomoku.player.human import Human
from gomoku.player.simple import Simple
from gomoku.player.threat_space import ThreatSpace
# from gomoku.board import Board

# g = Game(ThreatSpace(), ThreatSpace())
g = Game(ThreatSpace(), Human())
# g = Game(Human(), ThreatSpace())

g.play()
