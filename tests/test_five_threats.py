from gomoku.board import Board
from gomoku.threat.threat_search import get_fives

def test_fives_d2():
    b = Board(b1=26329679953269256590878443281372905617046033263622277107621691400, b2=182698855719568402303776577501133189974852648960, turns=24)
    assert set([158, 140, 70]) == set([t.gain_square for t in get_fives(b)])
    assert set([101, 70, 6, 171, 76]) == set([t.gain_square for t in get_fives(b, current=False)])

def test_fives_d1():
    b = Board(b1=210627797262243496972933896861861890712492219281965965622533750785, b2=1461523938416389008044623366763029326600029210624, turns=24)
    assert set([64, 153, 145]) == set([t.gain_square for t in get_fives(b)])
    assert set([96, 1, 176]) == set([t.gain_square for t in get_fives(b, current=False)])

def test_fives_h():
    b = Board(b1=1931279, b2=197460546878544725058596301906882060654875585745477675933925113856, turns=24)
    assert set([4, 10, 17]) == set([t.gain_square for t in get_fives(b)])
    assert set([78, 94, 212, 217]) == set([t.gain_square for t in get_fives(b, current=False)])

def test_fives_v():
    b = Board(b1=6917634588273770501, b2=26960769444537707362641678484230097234781136069450457969171361693696, turns=24)
    assert set([1, 76, 47]) == set([t.gain_square for t in get_fives(b)])
    assert set([120, 179, 124]) == set([t.gain_square for t in get_fives(b, current=False)])
