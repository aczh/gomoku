# from .. threat.threat_search import get_fours, get_threes, has_five
# import random
# score_five = 100000
# score_four = 10000
# score_three = 1000
# class Minimax:
#
#     def make_move(self, b):
#         best_move = None
#         best_score = -100000000
#         for m in self.valid_moves(b):
#             score = self.negamax(b, depth=2)
#             if score > best_score:
#                 best_score = score
#                 best_move = m
#         return m
#
#     def negamax(self, b, depth=0):
#         if depth == 0:
#             return self.eval(b)
#         best = -score_five
#         for m in self.valid_moves(b):
#             b.move(*m)
#             score = -self.negamax(b, depth - 1)
#             b.undo()
#             best = max(best, score)
#         return best
#
#     def eval(self, b):
#         if has_five(b):
#             return score_max
#         else:
#             fours = [item for sublist in get_fours(b) for item in sublist]
#             threes = [item for sublist in get_threes(b) for item in sublist]
#             return len(fours) * score_four + len(threes) * score_three
#
#     def valid_moves(self, b):
#         moves = [
#             (r, c)
#             for r in range(b.size) for c in range(b.size)
#             if b.is_valid_move(r, c)
#         ]
#         return moves
