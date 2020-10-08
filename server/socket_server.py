from flask_socketio import SocketIO, emit, join_room
from gomoku import Game
from gomoku.player import HumanSocket, Simple, ThreatSpace
socket = SocketIO()



games = {}

@socket.on('connect')
def on_connect():
    print('User connected')

@socket.on('start_game')
def start_game(data):
    username = data.get('username')
    print(f'Starting game for user: {username}')
    games[username] = Game(HumanSocket(socket), ThreatSpace())
    games[username].play()
