import json
from flask import Blueprint, request
from models import Game
from gomoku.board import Board
from gomoku.player.threat_space import ThreatSpace

api = Blueprint('game', __name__)

@api.route('/game', methods=["POST"])
def create_game():
    game = Game(**request.args.to_dict()).save()
    return game.to_json()

@api.route('/game', methods=["GET"])
def get_games():
    games = Game.objects()
    return games.to_json()

@api.route('/game/<id>/move', methods=["PUT"])
def make_move(id):
    row = int(request.args['row'])
    col = int(request.args['col'])

    game = Game.objects.get(id=id)
    game_json = json.loads(game.to_json())
    b = Board(b1=int(game_json['board1']), b2=int(game_json['board2']), turns=int(game_json['turns']))
    b.move(row, col)
    game.update(board1=bin(b.b1)[2:], board2=bin(b.b2)[2:], turns=b.turns)
    return game.to_json()

@api.route('/game/<id>/threat_space_move', methods=["PUT"])
def threat_space_move(id):
    game = Game.objects.get(id=id)
    game_json = json.loads(game.to_json())
    b = Board(b1=int(game_json['board1']), b2=int(game_json['board2']), turns=int(game_json['turns']))
    ts = ThreatSpace()
    move = ts.make_move(b)
    b.move_index(move)
    print(b)
    game.update(board1=bin(b.b1)[2:], board2=bin(b.b2)[2:], turns=b.turns)
    return game.to_json()
