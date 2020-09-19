from gomoku.board import Board
from gomoku.threat.threat_search import get_pattern

b = Board(size=15)

print(get_pattern(b))
