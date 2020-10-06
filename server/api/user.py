from flask import Blueprint, request
from models.user import User

api = Blueprint('users', __name__)

@api.route('/user', methods=["POST"])
def create_user():
    user = User(**request.args.to_dict()).save()
    return {}

@api.route('/user', methods=["GET"])
def get_users():
    users = User.objects()
    return users.to_json()
