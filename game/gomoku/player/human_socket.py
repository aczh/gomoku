from flask_socketio import SocketIO, emit, join_room

class HumanSocket:
    def __init__(self, socket, room):
        self.socket = socket
        self.room = room
        self.game = None
        self.last_board = None

    def request_move(self, b, game):
        print('Requesting move...')
        self.game = game
        self.last_board = b
        self.socket.emit('request_move', {
            'p1': bin(b.b1)[2:][::-1],
            'p2': bin(b.b2)[2:][::-1],
            'turns': b.turns,
            'history': game.history,
        }, room=self.room)
