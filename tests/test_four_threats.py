from gomoku.board import Board
from gomoku.threat.threat_search import get_fours
from gomoku.threat.threat import ThreatType

def test_fours():
    b = Board(b1=46075232374899851988888011134054464788371240387889679174276743175, b2=0, turns=24)
    assert {3, 4, 47, 49, 60, 75, 75, 75, 92, 93, 106, 109, 120, 122, 123, 136, 138, 150, 151, 152, 152, 152, 155, 165, 169, 170, 182, 182, 183, 195, 198, 200, 210, 211, 215, 216} == {t.gain_square for t in get_fours(b)}

    b = Board(b1=1131284383158329154918172611346496335385136781746103479376572416, b2=0, turns=0)
    assert {10, 11, 55, 57, 205, 208, 101, 102, 146, 148} == {t.gain_square for t in get_fours(b)}

    b = Board(b1=1131284383158329154918172611346496335385136781746103479376572416, b2=462798156746589199802099986564874898260710197218964532000459776, turns=0)
    assert set() == {t.gain_square for t in get_fours(b)}
