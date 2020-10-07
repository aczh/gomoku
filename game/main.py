from gomoku.game import Game
from gomoku.player.human import Human
from gomoku.player.simple import Simple
from gomoku.player.threat_space import ThreatSpace
from gomoku.player.negamax import Negamax
from gomoku.board import Board

g = Game(ThreatSpace(), Human())
# g = Game(ThreatSpace(), ThreatSpace())
# g = Game(Negamax(), Human())
g.b = Board(b1=170177529696935300553615692377276547072, b2=2596544577333540053640990932598784, turns=10)
# g = Game(Human(), ThreatSpace())

g.play()
