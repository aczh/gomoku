import mongoengine as me
from . base import Base

class Game(Base):
    board_size = me.IntField(default=15)
    board1 = me.StringField(default="0", max_length=226)
    board2 = me.StringField(default="0", max_length=226)
    turns = me.IntField(default=0)
    moves = me.ListField(me.IntField())

    player1_id = me.ReferenceField('User')
    player2_id = me.ReferenceField('User')
