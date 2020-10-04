
class ThreatSearcher:
    class __ThreatSearcher:
        def __init__(self):
            self.seen = {}

        def threes(self, b, current=True):
            if (b, current) in self.seen and self.seen[(b, current)][2]:
                print('threes hit')
            if (b, current) not in self.seen:
                self.seen[(b, current)] = [None] * len(ThreatType)
            if not self.seen[(b, current)][2]:
                self.seen[(b, current)][2] = _get_threes(b, current=current)
            return self.seen[(b, current)][2]

        # def fours(self, b, current=True):
        #     if (b, current) in self.seen and self.seen[2]:
        #         print('fours hit')
        #     if (b, current) not in self.seen:
        #         self.seen[(b, current)] = [None] * len(ThreatType)
        #     if not self.seen[1]:
        #         self.seen[(b, current)][1] = get_fours(b, current=current)
        #     return self.seen[(b, current)][1]
        #
        # def fives(self, b, current=True):
        #     if (b, current) in self.seen and self.seen[2]:
        #         print('fives hit')
        #     if (b, current) not in self.seen:
        #         self.seen[(b, current)] = [None] * len(ThreatType)
        #     if not self.seen[0]:
        #         self.seen[(b, current)][0] = get_fives(b, current=current)
        #     return self.seen[(b, current)][0]

    instance = None
    def __init__(self):
        if not ThreatSearcher.instance:
            ThreatSearcher.instance = ThreatSearcher.__ThreatSearcher()
        else:
            ThreatSearcher.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)


    def threats(self, b, current=True):
        return self.threes(b, current=current) + self.fours(b, current=current) + self.fives(b, current=current)

ts = ThreatSearcher()
def get_threes(board, current=True):
    return _get_threes(board, current=current)
    # return ts.threes(board, current=current)
