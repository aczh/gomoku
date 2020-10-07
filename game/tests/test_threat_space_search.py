from gomoku.board import Board
from gomoku.threat.threat_space import threat_space_search

def test_tss_1():
    # [(7, 6), (5, 8), (5, 7), (5, 6), (5, 5)]
    b = Board(b1=15577049031929511414266676075560960, b2=41538771009091192349931938353512448, turns=6)
    assert threat_space_search(b, depth=5)

    # [(5, 7), (6, 8), (5, 9)]
    # white threatens straight four
    b = Board(b1=6969238091508307294112410906664977964204032, b2=205615658366140053706398589785338065307463319552, turns=12)
    assert threat_space_search(b, depth=5)

    # [(0, 4), (4, 8), (7, 8)]
    b = Board(b1=316922321463614267476293976071, b2=28753546634630754380615942646379741989379916626753424690676020281344, turns=14)
    assert threat_space_search(b, depth=5)

    # [(7, 8), (5, 6)]
    b = Board(b1=680590695484625926093438556930779906048, b2=396155319976304968697169051648, turns=10)
    assert threat_space_search(b, depth=5)

    # [(7, 11), (8, 12), (7, 12)]
    # white threatens a straight four, win via stringing together five threats
    b = Board(b1=5846184955285236265145551303446056214553581060096, b2=340284963227828893675031342639189327872, turns=14)
    assert threat_space_search(b, depth=5)

def test_tss_should_fail():
    b = Board(b1=98653640321833131498996463652831232, b2=425355554958058671771561199724962775040, turns=8)
    assert not threat_space_search(b, depth=5)

    # # [(7, 5), (9, 7), (8, 6), (9, 5), (9, 4), (9, 6)]
    # # not sure if this fails or not...?
    # b = Board(b1=7788603744127269971470931581730816, b2=118842243771396506390315925505, turns=6)
    # assert threat_space_search(b, depth=5)


def test_tss_four_chains():
    # ensure tss doesn't report back a string of threats that can be thwarted by a defense of multiple five threats
    b = Board(b1=446646568860347136054359119660985614336, b2=11683103721656334534779806651777025, turns=22)
    assert threat_space_search(b, depth=5)

    # line: [(8, 5), (6, 11), (6, 10), (3, 10), (3, 7)], fails due to string of five threats
    b = Board(b1=446646568701890811025830444473897713664, b2=11683103721656334534779806651777024, turns=20)
    assert not threat_space_search(b, depth=5)

    # FLAW OF THREAT SPACE
    # (4, 6) allows the opponent to win with seq: [(9, 6), (5, 5), (7, 5), (6, 5), (7, 4)], skipping...
    # (8, 6) allows the opponent to win with seq: [(4, 6), (2, 4), (5, 8), (4, 8), (3, 8), (4, 7), (4, 5)], skipping...
    # b = Board(b1=170177529696935300553615692377276547072, b2=2596544574915688414411732583186432, turns=9)
