from flask_socketio import SocketIO, emit, join_room
from gomoku import Game
from gomoku.player import HumanSocket, Simple, ThreatSpace
socket = SocketIO()



games = {}

@socket.on('connect')
def on_connect():
    print('User connected')

def on_win(b):
    socket.emit('game_won', {
        'p1': bin(b.b1)[2:][::-1],
        'p2': bin(b.b2)[2:][::-1],
        'turns': b.turns,
    })

def on_draw(b):
    socket.emit('game_drawn')
    print("DRAW")

@socket.on('start_game')
def start_game(data):
    game_id = data.get('game_id')
    if game_id in games:
        print(f'Game already started for game_id: {game_id}')
    else:
        games[game_id] = Game(ThreatSpace(), HumanSocket(socket), on_win=on_win, on_draw=on_draw)
        # games[game_id] = Game(HumanSocket(socket), ThreatSpace())
    games[game_id].play()
