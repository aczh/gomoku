from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room
from gomoku import Game, who_won
from gomoku.player import HumanSocket, Simple, ThreatSpace, Negamax, AlphaBeta
socket = SocketIO()

games = {}

def on_win(game):
    socket.emit('game_won', {
        'p1': bin(game.b.b1)[2:][::-1],
        'p2': bin(game.b.b2)[2:][::-1],
        'turns': game.b.turns,
        'history': game.history,
        'winner': who_won(game.b)
    }, room=request.sid)

def on_draw(b):
    socket.emit('game_drawn', room=request.sid)

@socket.on('disconnect')
def on_disconnect():
    client_id = request.sid
    if client_id in games:
        del games[client_id]

@socket.on('move_made')
def move_made(data):
    client_id = request.sid
    try:
        move = int(data.get('move'))
        games[client_id].make_move(move)
    except Exception as e:
        print(f'Invalid move {move} from client {client_id}, exception {e}')

@socket.on('start_game')
def start_game():
    client_id = request.sid
    print(f"starting game for client: {client_id}")
    games[client_id] = Game(AlphaBeta(), HumanSocket(socket, room=client_id), on_win=on_win, on_draw=on_draw, verbose=1)
    games[client_id].play()
