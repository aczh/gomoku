from gomoku.board import Board
from gomoku.threat.threat_search import get_fives

def test_fives_d2():
    b = Board(b1=26329679953269256590878443281372905617046033263622277107621691400, b2=182698855719568402303776577501133189974852648960, turns=24)
    assert {158, 140, 70} == {t.gain_square for t in get_fives(b)}
    assert {101, 70, 6, 171, 76} == {t.gain_square for t in get_fives(b, current=False)}

def test_fives_d1():
    b = Board(b1=210627797262243496972933896861861890712492219281965965622533750785, b2=1461523938416389008044623366763029326600029210624, turns=24)
    assert {64, 153, 145} == {t.gain_square for t in get_fives(b)}
    assert {96, 1, 176} == {t.gain_square for t in get_fives(b, current=False)}

def test_fives_h():
    b = Board(b1=1931279, b2=197460546878544725058596301906882060654875585745477675933925113856, turns=24)
    assert {4, 10, 17} == {t.gain_square for t in get_fives(b)}
    assert {78, 94, 212, 217} == {t.gain_square for t in get_fives(b, current=False)}

def test_fives_v():
    b = Board(b1=6917634588273770501, b2=26960769444537707362641678484230097234781136069450457969171361693696, turns=24)
    assert {1, 76, 47} == {t.gain_square for t in get_fives(b)}
    assert {120, 179, 124} == {t.gain_square for t in get_fives(b, current=False)}

def test_fives():
    b = Board(b1=34588700701581312000, b2=0, turns=16)
    assert {0, 1, 2, 3, 4, 5, 15, 30, 45, 60, 20, 35, 50, 65, 75, 76, 77, 78, 79, 80} == {t.gain_square for t in get_fives(b)}

def test_fives_fail():
    b = Board(b1=34588700701581312000, b2=2380110754937072927146047, turns=36)
    assert set() == {t.gain_square for t in get_fives(b)}
