from gomoku.board import Board
from gomoku.threat_search import has_five, get_fours

def test_horizontal_fours():
    b = Board()

    b.move(1, 1)
    b.move(5, 15)

    b.move(1, 2)
    b.move(5, 14)

    b.move(1, 3)
    b.move(5, 13)

    b.move(1, 4)
    b.move(5, 12)

    print('')
    b.print()
    print(bin(get_fours(b)))

def test_horizontal_win():
    b = Board()

    b.move(1, 1)
    b.move(5, 15)

    b.move(1, 2)
    b.move(5, 14)

    b.move(1, 3)
    b.move(5, 13)

    b.move(1, 4)
    b.move(5, 12)

    assert not has_five(b)
    b.move(1, 5)

    assert not has_five(b, current=False)
    b.move(5, 11)

    assert has_five(b)
    assert has_five(b, current=False)

def test_vertical_win():
    b = Board()

    b.move(1, 1)
    b.move(15, 15)

    b.move(1, 2)
    b.move(15, 14)

    b.move(1, 3)
    b.move(15, 13)

    b.move(1, 4)
    b.move(15, 12)

    assert not has_five(b)
    b.move(1, 5)
    assert not has_five(b, current=False)
    b.move(15, 11)

    assert has_five(b)
    assert has_five(b, current=False)

def test_main_diag_win():
    b = Board()

    b.move(1, 1)
    b.move(15, 15)

    b.move(2, 2)
    b.move(14, 14)

    b.move(3, 3)
    b.move(13, 13)

    b.move(4, 4)
    b.move(12, 12)

    assert not has_five(b)
    b.move(5, 5)
    assert not has_five(b, current=False)
    b.move(11, 11)

    assert has_five(b)
    assert has_five(b, current=False)

def test_off_diag_win():
    b = Board()

    b.move(1, 5)
    b.move(15, 11)

    b.move(2, 4)
    b.move(14, 12)

    b.move(3, 3)
    b.move(13, 13)

    b.move(4, 2)
    b.move(12, 14)

    assert not has_five(b)
    b.move(5, 1)
    assert not has_five(b, current=False)
    b.move(11, 15)

    assert has_five(b)
    assert has_five(b, current=False)
