from flask import Flask
import mongoengine as me

from api.user import api as user
from api.game import api as game

# initialize flask
app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(game)

# connect mongoengine
me.connect('gomoku')

if __name__ == "__main__":
    app.run()
