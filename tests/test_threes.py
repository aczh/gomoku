from gomoku.board import Board
from gomoku.threat.threat_search import get_threes

def test_threes_h():
    b = Board()

    p1_moves = [
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
    ]

    p2_moves = [
        (5, 1),
        (5, 2),
        (5, 3),
        (5, 4),
    ]
    b.moves(p1=p1_moves, p2=p2_moves)

    p1_threes = get_threes(b)
    p2_threes = get_threes(b, current=False)
    b.print()

    print(p1_threes)
    print(p2_threes)
