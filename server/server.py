from flask import Flask
import mongoengine as me

from api.user import api as user

# initialize flask
app = Flask(__name__)
app.register_blueprint(user)

# connect mongoengine
me.connect('gomoku')

if __name__ == "__main__":
    app.run()
