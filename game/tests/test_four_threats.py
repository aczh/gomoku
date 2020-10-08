from gomoku import Board
from gomoku.threat.threat_search import get_fours
from gomoku.threat.threat import ThreatType

def test_fours_h():
    b = Board(b1=46075232374899851988888011134054464788371240387889679174276743175, b2=0, turns=0)
    assert {3, 4, 47, 49, 60, 75, 75, 75, 92, 93, 106, 109, 120, 122, 123, 136, 138, 150, 151, 152, 152, 152, 155, 165, 169, 170, 182, 182, 183, 195, 198, 200, 210, 211, 215, 216} == {t.gain_square for t in get_fours(b)}

    b = Board(b1=1131284383158329154918172611346496335385136781746103479376572416, b2=0, turns=0)
    assert {10, 11, 55, 57, 205, 208, 101, 102, 146, 148} == {t.gain_square for t in get_fours(b)}

    b = Board(b1=1131284383158329154918172611346496335385136781746103479376572416, b2=462798156746589199802099986564874898260710197218964532000459776, turns=0)
    assert set() == {t.gain_square for t in get_fours(b)}

def test_fours_v():
    b = Board(b1=1173762677155955597569688951786924451633037406068443423280421928960, b2=0, turns=0)
    assert {134, 145, 146, 148, 149, 150, 153, 157, 161, 165, 171, 173, 174, 177, 178, 183, 186, 188, 190, 192, 202, 204, 205, 209, 214, 215, 218, 220, 221, 223, 224} == {t.gain_square for t in get_fours(b)}

    b = Board(b1=664371307851597259337, b2=0, turns=0)
    assert {33, 36, 73, 45, 60, 51, 54, 24, 28, 63} == {t.gain_square for t in get_fours(b)}

    b = Board(b1=664371307851597259337, b2=9455129560741041930240, turns=0)
    assert set() == {t.gain_square for t in get_fours(b)}
