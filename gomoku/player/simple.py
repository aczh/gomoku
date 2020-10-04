from .. threat.threat_search import get_fives, get_fours, get_threes, get_threats
from .. utils import to_row, ThreatType
import random

class Simple:
    def make_move(self, b):
        m_threats = get_threats(b)
        m_threats.sort(key=lambda x: x.type, reverse=True)

        t_threats = get_threats(b, current=False)
        t_threats.sort(key=lambda x: x.type, reverse=True)

        m_best_index = -1 if not m_threats else m_threats[0].gain_square
        m_best_score = -1 if not m_threats else m_threats[0].type

        t_best_index = -1 if not t_threats else t_threats[0].gain_square
        t_best_score = -1 if not t_threats else t_threats[0].type

        if m_best_score != -1 and m_best_score >= t_best_score:
            print(f'Making {m_best_score.name}')
            return m_best_index
        elif t_best_score != -1:
            print(f'Blocking {t_best_score.name}')
            return t_best_index

        print('Random move...')
        return random.choice(self.valid_moves(b))

    def valid_moves(self, b):
        moves = [
            (r, c)
            for r in range(b.size) for c in range(b.size)
            if b.is_valid_move(r, c)
        ]
        return moves