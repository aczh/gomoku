from flask_socketio import SocketIO, emit, join_room
from gomoku.player import ThreatSpace

socket = SocketIO()

from . board import Board
from . threat.threat_search import has_five
from . utils import to_row


@socket.on('connect')
def on_connect():
    print('user connected')

@socket.on('move_made')
def on_move(data):
    print("MOOOOOVE")
    print(data.get('move'))
