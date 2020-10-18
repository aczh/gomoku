from gomoku import Board

def test_valid_moves():
    b = Board()

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

def test_valid_index():
    b = Board()

    assert b.is_valid_index(0)
    assert b.is_valid_index(1)
    assert b.is_valid_index(2)
    assert b.is_valid_index(224)
    assert not b.is_valid_index(-1)
    assert not b.is_valid_index(225)
    assert b.is_valid_index(1)
    b.move_index(1)
    assert not b.is_valid_index(1)

def test_force_index():
    b = Board()
    b.force_index(0)
    assert b.b1 == 1
    assert b.b2 == 0

    b.force_index(0, current=False)
    assert b.b2 == 1

def test_undo_move():
    b = Board()

    b.force_index(0)
    assert b.b1 == 1
    b.force_undo_index(0)
    assert b.b1 == 0

    b.force_index(1, current=False)
    b.force_index(4, current=False)
    b.force_index(225, current=False)
    b.force_undo_index(1)
    b.force_undo_index(4)
    b.force_undo_index(225)
    assert b.b2 == 0
