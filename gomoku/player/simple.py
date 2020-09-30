# from .. threat.threat_search import get_fours, get_threes
# import random
#
# class Simple:
#     def make_move(self, b):
#         # complete own four
#         m_fours = [item for sublist in get_fours(b) for item in sublist]
#         if m_fours:
#             return b.to_row(random.choice(m_fours))
#
#         # block four
#         t_fours = [item for sublist in get_fours(b, current=False) for item in sublist]
#         if t_fours:
#             return b.to_row(random.choice(t_fours))
#
#         # make three
#         m_threes = [item for sublist in get_threes(b) for item in sublist]
#         if m_threes:
#             return b.to_row(random.choice(m_threes))
#
#         # block three
#         t_threes = [item for sublist in get_threes(b, current=False) for item in sublist]
#         if t_threes:
#             return b.to_row(random.choice(t_threes))
#
#         return random.choice(self.valid_moves(b))
#
#     def valid_moves(self, b):
#         moves = [
#             (r, c)
#             for r in range(b.size) for c in range(b.size)
#             if b.is_valid_move(r, c)
#         ]
#         return moves
