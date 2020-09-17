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
