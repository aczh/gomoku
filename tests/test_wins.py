from gomoku.board import Board
from gomoku.threat.threat_search import has_five

def test_h_win():
    b = Board()

    b.move(1, 0)
    b.move(5, 11)

    b.move(1, 1)
    b.move(5, 12)

    b.move(1, 2)
    b.move(5, 13)

    b.move(1, 3)
    b.move(5, 14)

    b.move(0, 14)
    b.move(6, 0)

    assert not has_five(b)
    assert not has_five(b, current=False)

    b.move(1, 4)
    b.move(5, 10)

    assert has_five(b)
    assert has_five(b, current=False)

def test_v_win():
    b = Board()

    b.move(0, 0)
    b.move(14, 14)

    b.move(1, 0)
    b.move(13, 14)

    b.move(2, 0)
    b.move(12, 14)

    b.move(3, 0)
    b.move(11, 14)

    b.move(14, 0)
    b.move(0, 14)

    assert not has_five(b)
    assert not has_five(b, current=False)

    b.move(4, 0)
    b.move(10, 14)

    assert has_five(b)
    assert has_five(b, current=False)

def test_d1_win():
    b = Board()

    b.move(1, 11)
    b.move(11, 1)

    b.move(2, 12)
    b.move(12, 2)

    b.move(3, 13)
    b.move(13, 3)

    b.move(4, 14)
    b.move(10, 0)

    b.move(5, 0)
    b.move(8, 14)

    assert not has_five(b)
    assert not has_five(b, current=False)

    b.move(0, 10)
    b.move(14, 4)

    assert has_five(b)
    assert has_five(b, current=False)

def test_d2_win():
    b = Board()

    b.move(1, 3)
    b.move(13, 11)

    b.move(2, 2)
    b.move(12, 12)

    b.move(3, 1)
    b.move(11, 13)

    b.move(4, 0)
    b.move(10, 14)

    b.move(4, 14)
    b.move(10, 0)

    assert not has_five(b)
    assert not has_five(b, current=False)

    b.move(0, 4)
    b.move(14, 10)

    assert has_five(b)
    assert has_five(b, current=False)
