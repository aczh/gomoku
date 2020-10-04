from gomoku.game import Game
from gomoku.player.human import Human
from gomoku.player.simple import Simple
from gomoku.player.threat_space import ThreatSpace
from gomoku.board import Board

# g = Game(ThreatSpace(), ThreatSpace())
g = Game(ThreatSpace(), Human())
# g.b = Board(b1=45671927527737059040482067350624460704441171968, b2=170143780005053824545212346276364943360, turns=30)
# g = Game(Human(), ThreatSpace())

g.play()
