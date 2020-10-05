from gomoku.game import Game
from gomoku.player.human import Human
from gomoku.player.simple import Simple
from gomoku.player.threat_space import ThreatSpace
from gomoku.board import Board

# g = Game(ThreatSpace(), ThreatSpace())
g = Game(ThreatSpace(), Human())
# g.b = Board(b1=170159356657930428656915835640124276736, b2=20769266669555379696147353909067776, turns=9)

# g = Game(Human(), ThreatSpace())

g.play()
