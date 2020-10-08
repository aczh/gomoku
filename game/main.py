from gomoku.game import Game
from gomoku.player.human import Human
from gomoku.player.simple import Simple
from gomoku.player.threat_space import ThreatSpace
from gomoku.player.negamax import Negamax
from gomoku.board import Board

g = Game(ThreatSpace(), Human())
# g = Game(Simple(), Simple())
# g = Game(Human(), Human())
# g = Game(ThreatSpace(), Human())
# g = Game(Human(), ThreatSpace())

g.play()
