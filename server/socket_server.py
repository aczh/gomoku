from flask_socketio import SocketIO, emit, join_room
from gomoku import Game, who_won
from gomoku.player import HumanSocket, Simple, ThreatSpace
socket = SocketIO()

games = {}

def on_win(game):
    socket.emit('game_won', {
        'p1': bin(game.b.b1)[2:][::-1],
        'p2': bin(game.b.b2)[2:][::-1],
        'turns': game.b.turns,
        'history': game.history,
        'winner': who_won(game.b)
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
    games[game_id].play()
