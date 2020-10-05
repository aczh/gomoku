from gomoku.board import Board
from gomoku.threat.threat_search import get_straight_fours
from gomoku.threat.threat import ThreatType

def test_straight_fours_h():
    b = Board(b1=23037063802496884590169568565107503057583874975924630746556268551, b2=23589953333756809820333638239253801952324717697362898023789247885312, turns=40)
    assert {94, 214} == {t.gain_square for t in get_straight_fours(b)}
    assert {91, 92, 93, 211, 212, 213} == {rs for t in get_straight_fours(b) for rs in t.rest_squares}

    assert {100, 220} == {t.gain_square for t in get_straight_fours(b, current=False)}
    assert {101, 102, 103, 221, 222, 223} == {rs for t in get_straight_fours(b, current=False) for rs in t.rest_squares}

def test_straight_fours_v():
    b = Board(b1=26328072917139296765823359254099040467454077075544439471194406917, b2=8244648812060184370595159831380097666673487620484721118552260624, turns=40)
    assert {25, 68, 85} == {t.gain_square for t in get_straight_fours(b)}
    assert {23, 38, 53, 40, 55, 70} == {rs for t in get_straight_fours(b) for rs in t.rest_squares}

    assert {145, 158, 205} == {t.gain_square for t in get_straight_fours(b, current=False)}
    assert {160, 175, 190, 173, 188, 203} == {rs for t in get_straight_fours(b, current=False) for rs in t.rest_squares}

def test_straight_fours_d1():
    b = Board(b1=803481282280894275168001443658667529825135083300549803704321, b2=26960358049567071837410330346816762151573619369275773304076916228096, turns=28)
    assert {151} == {t.gain_square for t in get_straight_fours(b)}
    assert {167, 183, 199} == {rs for t in get_straight_fours(b) for rs in t.rest_squares}

    assert {114, 178} == {t.gain_square for t in get_straight_fours(b, current=False)}
    assert {130, 146, 162} == {rs for t in get_straight_fours(b, current=False) for rs in t.rest_squares}

def test_straight_fours_d2():
    b = Board(b1=324538361983543588175592382595076, b2=6740398071174139633051988437119323087006219085847281297982551490560, turns=18)
    assert {34, 66, 122} == {t.gain_square for t in get_straight_fours(b)}
    assert {48, 62, 76, 80, 94, 108} == {rs for t in get_straight_fours(b) for rs in t.rest_squares}

    assert {205, 101, 157} == {t.gain_square for t in get_straight_fours(b, current=False)}
    assert {163, 177, 191, 115, 129, 143} == {rs for t in get_straight_fours(b, current=False) for rs in t.rest_squares}
