from .. import utils
from .. utils import ThreatType


class Threat:
    def __init__(self):
        self.type = None
        self.gain_square = -1
        self.cost_squares = []
        self.rest_squares = []

    def __str__(self):
        return (
            f'type: {self.type}, '
            f'gain: {utils.to_row(self.gain_square)}, '
            f'cost: {[utils.to_row(s) for s in self.cost_squares]}, '
            f'rest: {[utils.to_row(s) for s in self.rest_squares]}'
        )

class Five(Threat):
    def __init__(self, initial, inc, gain):
        super()
        self.type = ThreatType.FIVE
        self.gain_square = gain
        self.rest_squares = [i for i in range(initial, initial + 5 * inc, inc) if i != gain]
        self.cost_squares = []

class Four(Threat):
    def __init__(self, initial, inc, gain, cost):
        super()
        self.type = ThreatType.FOUR
        self.gain_square = gain
        self.rest_squares = [i for i in range(initial, initial + 5 * inc, inc) if i != gain and i != cost]
        self.cost_squares = [cost]

class StraightFour(Four):
    def __init__(self, initial, inc, gain, cost):
        super().__init__(initial, inc, gain, cost)
        self.type = ThreatType.STRAIGHT_FOUR
