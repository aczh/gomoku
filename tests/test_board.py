from gomoku.board import Board

def test_valid_moves():
    b = Board(size=15)

    assert not b.is_valid_move(15, 15)
    assert not b.is_valid_move(15, 14)
    assert not b.is_valid_move(14, 15)
    assert not b.is_valid_move(-1, -1)
    assert not b.is_valid_move(-1, 0)
    assert not b.is_valid_move(0, -1)

    assert b.is_valid_move(0, 0)
    b.move(0, 0)
    assert not b.is_valid_move(0, 0)

    assert b.is_valid_move(14, 14)
    b.move(14, 14)
    assert not b.is_valid_move(14, 14)
