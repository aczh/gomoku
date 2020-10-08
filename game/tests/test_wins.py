from gomoku import Board
from gomoku.threat.threat_search import has_five

def test_win_h():
    b = Board(b1=507904, b2=2398508826115424282617053184, turns=10)
    assert not has_five(b)
    assert not has_five(b, current=False)

    b = Board(b1=1032192, b2=2437194452343092416207650816, turns=12)
    assert has_five(b)
    assert has_five(b, current=False)

def test_win_v():
    b = Board(b1=1645504557321206042154969182557350504982735865633615048794472449, b2=26960769444538473587005248571383246215233876609474620418452514422784, turns=10)
    assert not has_five(b)
    assert not has_five(b, current=False)

    b = Board(b1=1645504557321206042154969182557350504982735866786536553401319425, b2=26960769444538473610389274768677692906492833932935148732947435110400, turns=12)
    assert has_five(b)
    assert has_five(b, current=False)

def test_win_d1():
    b = Board(b1=56668686029210007896064, b2=401740641140448564499572520681256201108752761030936174264320, turns=10)
    assert not has_five(b)
    assert not has_five(b, current=False)

    b = Board(b1=56668686029210007897088, b2=26328474657780437123044006493438289335924882602898308749752008704, turns=12)
    assert has_five(b)
    assert has_five(b, current=False)

def test_win_d2():
    b = Board(b1=18890618923356227108864, b2=102850312317458034985366611441495511031023819840037617343135744, turns=10)
    assert not has_five(b)
    assert not has_five(b, current=False)

    b = Board(b1=18890618923356227108880, b2=1685099517009232445201673809550168412613352550228625817686318776320, turns=12)
    assert has_five(b)
    assert has_five(b, current=False)
