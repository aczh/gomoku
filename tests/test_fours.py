from gomoku.board import Board
from gomoku.threat.threat_search import get_fours

def test_fours_d2():
    b = Board()

    p1_moves = [
        (0, 3),
        (1, 2),
        (2, 1),
        (3, 0),

        (5, 9),
        (6, 8),
        (7, 7),
        (8, 6),

        (14, 4),
        (13, 5),
        (12, 6),
        (11, 7),
    ]

    p2_moves = [
        (1, 5),
        (2, 4),
        (3, 3),
        (4, 2),

        (0, 14),
        (1, 13),
        (2, 12),
        (3, 11),

        (7, 10),
        (8, 9),
        (9, 8),
        (10, 7),
    ]

    b.moves(p1=p1_moves, p2=p2_moves)

    p1_fours = get_fours(b)
    p2_fours = get_fours(b, current=False)

    assert set([158, 140, 70]) == set(p1_fours[3])
    assert set([101, 70, 6, 171, 76]) == set(p2_fours[3])

def test_fours_d1():
    b = Board()

    p1_moves = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),

        (5, 6),
        (6, 7),
        (7, 8),
        (8, 9),

        (14, 7),
        (13, 6),
        (12, 5),
        (11, 4),
    ]

    p2_moves = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),

        (0, 11),
        (1, 12),
        (2, 13),
        (3, 14),

        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
    ]

    b.moves(p1=p1_moves, p2=p2_moves)

    p1_fours = get_fours(b)
    p2_fours = get_fours(b, current=False)

    assert set([64, 153, 145]) == set(p1_fours[2])
    assert set([96, 1, 176]) == set(p2_fours[2])

def test_fours_h():
    b = Board()

    p1_moves = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),

        (1, 1),
        (1, 3),
        (1, 4),
        (1, 5),

        (0, 14),
        (0, 13),
        (0, 12),
        (0, 11),
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

        (14, 3),
        (14, 4),
        (14, 5),
        (14, 6),
    ]

    b.moves(p1=p1_moves, p2=p2_moves)

    p1_fours = get_fours(b)
    p2_fours = get_fours(b, current=False)

    assert set([4, 10, 17]) == set(p1_fours[0])
    assert set([78, 94, 212, 217]) == set(p2_fours[0])

def test_fours_v():
    b = Board()
    p1_moves = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),

        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),

        (0, 2),
        (1, 2),
        (2, 2),
        (4, 2),
    ]

    p2_moves = [
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),

        (6, 4),
        (7, 4),
        (9, 4),
        (10, 4),

        (14, 14),
        (13, 14),
        (12, 14),
        (10, 14),
    ]

    b.moves(p1=p1_moves, p2=p2_moves)
    p1_fours = get_fours(b)
    p2_fours = get_fours(b, current=False)

    assert set([1, 76, 47]) == set(p1_fours[1])
    assert set([120, 179, 124]) == set(p2_fours[1])
