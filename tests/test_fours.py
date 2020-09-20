from gomoku.board import Board
from gomoku.threat.threat_search import get_fours

def test_fours_unblockable():
        b = Board()

        p1_moves = [
            (0, 2),
            (0, 3),
            (0, 4),
            (0, 5),

            (1, 1),
            (1, 3),
            (1, 4),
            (1, 5),
        ]

        p2_moves = [
            (5, 1),
            (5, 2),
            (5, 4),
            (5, 5),

            (6, 1),
            (6, 2),
            (6, 3),
            (6, 5),
        ]

        b.moves(p1=p1_moves, p2=p2_moves)

        # b.move(1, 0)
        # b.move(5, 11)
        #
        # b.move(1, 1)
        # b.move(5, 12)
        #
        # b.move(1, 2)
        # b.move(5, 13)
        #
        # b.move(1, 3)
        # b.move(5, 14)


        print('')
        b.print()

        print(get_fours(b))
        print(get_fours(b, current=False))
