from gomoku.game import Game
from gomoku.player.human import Human
from gomoku.player.simple import Simple
from gomoku.player.threat_space import ThreatSpace
# from gomoku.player.minimax import Minimax

g = Game(Human(), ThreatSpace())
g.play()
