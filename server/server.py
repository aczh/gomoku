from flask import Flask, render_template
import mongoengine as me

from api.user import api as user
from api.game import api as game

# initialize flask
app = Flask(__name__, static_folder='../static/build', template_folder='../static/public')
app.register_blueprint(user)
app.register_blueprint(game)

# connect mongoengine
me.connect('gomoku')

@app.route('/', methods=["GET"])
def serve_bundle():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
