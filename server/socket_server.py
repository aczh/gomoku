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
    if username in games:
        print(f'Game already started for user: {username}')
    else:
        games[username] = Game(ThreatSpace(), HumanSocket(socket))
        # games[username] = Game(HumanSocket(socket), ThreatSpace())
    games[username].play()
