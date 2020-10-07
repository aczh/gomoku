from flask_socketio import SocketIO, emit, join_room

class HumanSocket:
    def __init__(self, socket):
        self.socket = socket

    def make_move(self, b):
        socket.emit('make_move')
