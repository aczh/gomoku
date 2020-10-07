from flask import Blueprint, request
from models import User

api = Blueprint('user', __name__)

@api.route('/user', methods=["POST"])
def create_user():
    user = User(**request.args.to_dict()).save()
    return user.to_json()

@api.route('/user', methods=["GET"])
def get_users():
    users = User.objects()
    return users.to_json()
