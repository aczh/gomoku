import mongoengine as me
from . base import Base

class User(Base):
    username = me.StringField(max_length=50, required=True, unique=True)
    me.ListField(me.ReferenceField('Game'))
