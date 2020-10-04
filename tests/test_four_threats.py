# from gomoku.board import Board
# from gomoku.threat.threat_search import get_fours
# from gomoku.utils import ThreatType
#
# def test_fours_h():
#     b = Board(b1=23037063802496884590169568565107503057583874975924630746556268551, b2=23589953333756809820333638239253801952324717697362898023789247885312, turns=40)
#     assert set([94, 214]) == set([t.gain_square for t in get_fours(b) if t.type == ThreatType.STRAIGHT_FOUR])
#     assert set([91, 92, 93, 211, 212, 213]) == set([rs for t in get_fours(b) for rs in t.rest_squares if t.type == ThreatType.STRAIGHT_FOUR])
#
#     assert set([100, 220]) == set([t.gain_square for t in get_fours(b, current=False) if t.type == ThreatType.STRAIGHT_FOUR])
#     assert set([101, 102, 103, 221, 222, 223]) == set([rs for t in get_fours(b, current=False) for rs in t.rest_squares if t.type == ThreatType.STRAIGHT_FOUR])
