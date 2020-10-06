import mongoengine as me
from . base import Base

class Game(Base):
    board_size = me.IntField(default=15)
    board1 = me.IntField(default=0)
    board2 = me.IntField(default=1)
    moves = me.ListFIeld(me.IntField())
