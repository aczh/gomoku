from gomoku.board import Board

def test_valid_moves():
    b = Board(size=15)

    assert not b.is_valid_move(16, 16)
    assert not b.is_valid_move(16, 15)
    assert not b.is_valid_move(15, 16)
    assert not b.is_valid_move(0, 0)
    assert not b.is_valid_move(0, 1)
    assert not b.is_valid_move(1, 0)

    assert b.is_valid_move(1, 1)
    b.move(1, 1)
    assert not b.is_valid_move(1, 1)

    assert b.is_valid_move(15, 15)
    b.move(15, 15)
    assert not b.is_valid_move(15, 15)

def test_horizontal_win():
    b = Board()
    assert not b.check_win(b.b1)
    assert not b.check_win(b.b2)

    b.move(1, 1)
    b.move(5, 15)

    b.move(1, 2)
    b.move(5, 14)

    b.move(1, 3)
    b.move(5, 13)

    b.move(1, 4)
    b.move(5, 12)

    b.move(1, 5)
    b.move(5, 11)

    assert b.check_win(b.b1)
    assert b.check_win(b.b2)

def test_vertical_win():
    b = Board()
    assert not b.check_win(b.b1)
    assert not b.check_win(b.b2)

    b.move(1, 1)
    b.move(15, 15)

    b.move(1, 2)
    b.move(15, 14)

    b.move(1, 3)
    b.move(15, 13)

    b.move(1, 4)
    b.move(15, 12)

    b.move(1, 5)
    b.move(15, 11)

    assert b.check_win(b.b1)
    assert b.check_win(b.b2)

def test_main_diag_win():
    b = Board()
    assert not b.check_win(b.b1)
    assert not b.check_win(b.b2)

    b.move(1, 1)
    b.move(15, 15)

    b.move(2, 2)
    b.move(14, 14)

    b.move(3, 3)
    b.move(13, 13)

    b.move(4, 4)
    b.move(12, 12)

    b.move(5, 5)
    b.move(11, 11)

    assert b.check_win(b.b1)
    assert b.check_win(b.b2)

def test_off_diag_win():
    b = Board()
    assert not b.check_win(b.b1)
    assert not b.check_win(b.b2)
    
    b.move(1, 5)
    b.move(15, 11)

    b.move(2, 4)
    b.move(14, 12)

    b.move(3, 3)
    b.move(13, 13)

    b.move(4, 2)
    b.move(12, 14)

    b.move(5, 1)
    b.move(11, 15)

    assert b.check_win(b.b1)
    assert b.check_win(b.b2)
