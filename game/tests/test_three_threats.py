from gomoku import Board
from gomoku.threat.threat_search import get_threes
from gomoku.threat.threat import ThreatType

def test_threes_h():
    b = Board(b1=15204462119094246358024271079344809213670845688342580052801852813318, b2=3371587417504494954974007377922711019190415832469971198715786953728, turns=0)
    threes = get_threes(b)
    assert {3, 47, 136, 139, 183, 212, 215} == {t.gain_square for t in threes if t.type == ThreatType.THREE}
    assert {4, 49, 61, 62, 76, 78, 92, 93, 140, 152, 167, 181, 185, 211, 216} == {t.gain_square for t in threes if t.type == ThreatType.BROKEN_THREE}

    b = Board(b1=20229833027711983473746581876392566992724233432663832027907085044754, b2=26329629638371122386643511463646460973608826515457406418314821640, turns=0)
    threes = get_threes(b)
    assert {9, 12, 41, 85, 88, 177, 221} == {t.gain_square for t in threes if t.type == ThreatType.THREE}
    assert {8, 13, 39, 43, 57, 72, 84, 131, 132, 146, 148, 162, 163, 175, 220} == {t.gain_square for t in threes if t.type == ThreatType.BROKEN_THREE}

def test_threes_v():
    b = Board(b1=3672891476010151502557879622480703580559875690609078528802884, b2=17611836739078791179946, turns=0)
    threes = get_threes(b)
    assert {149, 159, 165, 177, 183, 194, 204} == {t.gain_square for t in threes if t.type == ThreatType.THREE}
    assert {134, 144, 147, 150, 153, 170, 171, 184, 186, 190, 191, 199, 200, 207, 209} == {t.gain_square for t in threes if t.type == ThreatType.BROKEN_THREE}

    b = Board(b1=7162319788504155982827805124327059692777502629711063535409881415680, b2=17999077334328285453399166571313118630170740211630907907770643644416, turns=0)
    threes = get_threes(b)
    assert {20, 30, 41, 47, 59, 65, 75} == {t.gain_square for t in threes if t.type == ThreatType.THREE}
    assert {15, 17, 24, 25, 33, 34, 38, 40, 53, 54, 71, 74, 77, 80, 90} == {t.gain_square for t in threes if t.type == ThreatType.BROKEN_THREE}

def test_threes_d1():
    b = Board(b1=3163070797083699366456852580076715060144882955992810192896, b2=7831503478338133203954702522408954521915777935516552538915789684962197025662160732418, turns=0)
    threes = get_threes(b)
    assert {34, 48, 62, 64, 106, 154, 168} == {t.gain_square for t in threes if t.type == ThreatType.THREE}
    assert {18, 36, 64, 92, 92, 94, 108, 136, 170, 200} == {t.gain_square for t in threes if t.type == ThreatType.BROKEN_THREE}

    b = Board(b1=414596341970474834699697668392083915017612862765197491599048704, b2=13585493739536204692095844132594942219330080041750970058950630058580, turns=0)
    threes = get_threes(b)
    assert {56, 70, 118, 160, 162, 176, 190} == {t.gain_square for t in threes if t.type == ThreatType.THREE}
    assert {24, 54, 88, 116, 130, 132, 132, 160, 188, 206} == {t.gain_square for t in threes if t.type == ThreatType.BROKEN_THREE}

def test_threes_d2():
    b = Board(b1=2111073932812428422906442112647773728497144798729340750659584, b2=1097003038214090590529523847971122934742660962230003673897893888, turns=0)
    threes = get_threes(b)
    assert {152, 154, 160, 168, 176, 184, 202} == {t.gain_square for t in threes if t.type == ThreatType.THREE}
    assert {122, 146, 148, 154, 156, 166, 172, 186, 186, 204} == {t.gain_square for t in threes if t.type == ThreatType.BROKEN_THREE}

    b = Board(b1=3181004167481621677113856045145735373470694090211328, b2=2095061076360499789054781174343030509139193965558905864192, turns=0)
    threes = get_threes(b)
    assert {22, 40, 48, 56, 64, 70, 72} == {t.gain_square for t in threes if t.type == ThreatType.THREE}
    assert {20, 38, 38, 52, 58, 68, 70, 76, 78, 102} == {t.gain_square for t in threes if t.type == ThreatType.BROKEN_THREE}
