from gomoku.board import Board
from gomoku.threat.threat_search import get_straight_fours
from gomoku.utils import ThreatType

def test_straight_fours_h():
    b = Board(b1=23037063802496884590169568565107503057583874975924630746556268551, b2=23589953333756809820333638239253801952324717697362898023789247885312, turns=40)
    assert set([94, 214]) == set([t.gain_square for t in get_straight_fours(b)])
    assert set([91, 92, 93, 211, 212, 213]) == set([rs for t in get_straight_fours(b) for rs in t.rest_squares])

    assert set([100, 220]) == set([t.gain_square for t in get_straight_fours(b, current=False)])
    assert set([101, 102, 103, 221, 222, 223]) == set([rs for t in get_straight_fours(b, current=False) for rs in t.rest_squares])

def test_straight_fours_v():
    b = Board(b1=26328072917139296765823359254099040467454077075544439471194406917, b2=8244648812060184370595159831380097666673487620484721118552260624, turns=40)
    assert set([25, 68, 85]) == set([t.gain_square for t in get_straight_fours(b)])
    assert set([23, 38, 53, 40, 55, 70]) == set([rs for t in get_straight_fours(b) for rs in t.rest_squares])

    assert set([145, 158, 205]) == set([t.gain_square for t in get_straight_fours(b, current=False)])
    assert set([160, 175, 190, 173, 188, 203]) == set([rs for t in get_straight_fours(b, current=False) for rs in t.rest_squares])

def test_straight_fours_d1():
    b = Board(b1=803481282280894275168001443658667529825135083300549803704321, b2=26960358049567071837410330346816762151573619369275773304076916228096, turns=28)
    assert set([151]) == set([t.gain_square for t in get_straight_fours(b)])
    assert set([167, 183, 199]) == set([rs for t in get_straight_fours(b) for rs in t.rest_squares])

    assert set([114, 178]) == set([t.gain_square for t in get_straight_fours(b, current=False)])
    assert set([130, 146, 162]) == set([rs for t in get_straight_fours(b, current=False) for rs in t.rest_squares])

def test_straight_fours_d2():
    b = Board(b1=324538361983543588175592382595076, b2=6740398071174139633051988437119323087006219085847281297982551490560, turns=18)
    assert set([34, 66, 122]) == set([t.gain_square for t in get_straight_fours(b)])
    assert set([48, 62, 76, 80, 94, 108]) == set([rs for t in get_straight_fours(b) for rs in t.rest_squares])

    assert set([205, 101, 157]) == set([t.gain_square for t in get_straight_fours(b, current=False)])
    assert set([163, 177, 191, 115, 129, 143]) == set([rs for t in get_straight_fours(b, current=False) for rs in t.rest_squares])
