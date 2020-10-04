import gmpy2
from . import threat
from .. import utils
import operator
import functools
from .. utils import ThreatType, is_continuous, get_ones, to_row

def has_five(_b, current=True):
    for b in _b.get_boards(current=current):
        if b & (b >> _b.size) & (b >> _b.size * 2) & (b >> _b.size * 3) & (b >> _b.size * 4):
            return True
