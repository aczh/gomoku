import mongoengine as me
from flask import Flask, render_template

from socket_server import socket
from api.user import api as user
from api.game import api as game

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# initialize flask
app = Flask(__name__, static_folder='../static/build', template_folder='../static/public')
app.register_blueprint(user)
app.register_blueprint(game)

# connect mongoengine
me.connect('gomoku')

# connect socketio
socket.init_app(app)

# serve webpack bundle
@app.route('/', methods=["GET"])
def serve_bundle():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
