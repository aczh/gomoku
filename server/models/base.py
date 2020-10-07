import mongoengine as me
from . utils import utcnow

class Base(me.Document):
    created_at = me.DateTimeField(default=utcnow)
    updated_at = me.DateTimeField(default=utcnow)

    meta = {
        'abstract': True
    }
